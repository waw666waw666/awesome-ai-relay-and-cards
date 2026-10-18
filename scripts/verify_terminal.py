#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_terminal.py - 终端发卡店铺落地页穿透验真脚本
用于穿透比价网历史缓存，直连最终售卖落地页，提取真实结算价格、实时库存、交付规格与质保条款。
采用纯 Python 标准库实现，零外部第三方依赖。
"""

import sys
import os
import re
import json
import argparse
import urllib.request
import urllib.error
from urllib.parse import urlparse, urljoin
from html.parser import HTMLParser

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)


class TextExtractor(HTMLParser):
    """提取 HTML 中的纯文本"""
    def __init__(self):
        super().__init__()
        self.texts = []

    def handle_data(self, data):
        cleaned = data.strip()
        if cleaned:
            self.texts.append(cleaned)

    def get_text(self):
        return " ".join(self.texts)


def fetch_url(url, timeout=10, headers=None):
    """标准库 HTTP 请求包装"""
    req_headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json, text/html, application/xhtml+xml, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }
    if headers:
        req_headers.update(headers)

    req = urllib.request.Request(url, headers=req_headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            charset = resp.headers.get_content_charset() or "utf-8"
            body = resp.read().decode(charset, errors="replace")
            return {
                "status_code": resp.status,
                "headers": dict(resp.headers),
                "body": body,
                "final_url": resp.geturl(),
                "error": None
            }
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8", errors="replace")
        except Exception:
            pass
        return {
            "status_code": e.code,
            "headers": dict(e.headers),
            "body": body,
            "final_url": url,
            "error": str(e)
        }
    except Exception as e:
        return {
            "status_code": 0,
            "headers": {},
            "body": "",
            "final_url": url,
            "error": str(e)
        }


def check_cloudflare(response):
    """检测是否被 Cloudflare 5秒盾/验证码拦截"""
    body = response.get("body", "").lower()
    headers = response.get("headers", {})
    code = response.get("status_code", 0)

    is_cf_server = "cloudflare" in headers.get("Server", "").lower() or "cf-ray" in headers
    if code in (403, 503) and is_cf_server:
        if any(kw in body for kw in ["just a moment...", "turnstile", "cf-mitigated", "security check"]):
            return True
    return False


def probe_rest_api(base_url, sku_kw=None):
    """Level 1: 嗅探常见发卡 REST API (如 BuyAI catalog)"""
    parsed = urlparse(base_url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    
    candidate_endpoints = [
        urljoin(origin, "/api/catalog"),
        urljoin(origin, "/api/v1/goods"),
        urljoin(origin, "/api/goods/list"),
    ]

    for endpoint in candidate_endpoints:
        res = fetch_url(endpoint, timeout=6)
        if res["status_code"] == 200 and res["body"]:
            try:
                data = json.loads(res["body"])
                # 针对 BuyAI 等结构: {"categories": [...], "items": [...]} 或 直接是 list
                items = []
                if isinstance(data, list):
                    items = data
                elif isinstance(data, dict):
                    for k in ["products", "items", "goods", "data", "list"]:
                        if k in data:
                            val = data[k]
                            if isinstance(val, list):
                                items = val
                                break
                            elif isinstance(val, dict):
                                for sub_k in ["items", "products", "list"]:
                                    if sub_k in val and isinstance(val[sub_k], list):
                                        items = val[sub_k]
                                        break
                                if items:
                                    break

                if not items:
                    continue

                matched = []
                for item in items:
                    name = item.get("name") or item.get("title") or item.get("goods_name") or ""
                    desc = item.get("description") or ""
                    notes_val = item.get("notes") or item.get("buy_notes") or ""
                    notes_text = " | ".join(notes_val) if isinstance(notes_val, list) else str(notes_val)
                    full_text = f"{name} {desc} {notes_text}"

                    if sku_kw and sku_kw.lower() not in full_text.lower():
                        continue

                    # 提取价格 (考虑分或元)
                    price = None
                    if "price_fen" in item:
                        price = round(item["price_fen"] / 100.0, 2)
                    elif "price" in item:
                        try:
                            price = float(item["price"])
                        except Exception:
                            pass

                    # 提取库存
                    stock = item.get("stock")
                    if stock is None:
                        stock = item.get("in_stock_count") or item.get("quantity")
                    available = item.get("available", True) if stock is None else (stock > 0)

                    features = item.get("features") or []
                    if isinstance(features, str):
                        features = [features]

                    matched.append({
                        "name": name,
                        "real_price": price,
                        "in_stock": bool(available),
                        "stock_count": stock,
                        "features": features,
                        "notes": notes_text,
                        "source": f"REST_API ({endpoint})"
                    })

                if matched:
                    return matched
            except Exception:
                continue
    return None


def probe_embedded_json(html_body, sku_kw=None):
    """Level 2: 页面嵌入状态嗅探 (__NEXT_DATA__, window.goods 等)"""
    next_match = re.search(r'<script id="__NEXT_DATA__" type="application/json">({.*?})</script>', html_body)
    if next_match:
        try:
            next_data = json.loads(next_match.group(1))
            # 搜索 props 树
            json_str = json.dumps(next_data, ensure_ascii=False)
            if sku_kw and sku_kw.lower() in json_str.lower():
                pass # 可在此递归提取
        except Exception:
            pass

    return None


def probe_dom_regex(html_body, sku_kw=None):
    """Level 3: 语义正则与文本模式兜底分析"""
    parser = TextExtractor()
    try:
        parser.feed(html_body)
        raw_text = parser.get_text()
    except Exception:
        raw_text = html_body

    # 寻找包含 SKU 关键词的周边文本片段
    if sku_kw and sku_kw.lower() in raw_text.lower():
        # 寻找价格: ¥ 20 / ¥20 / 20.00元
        price_match = re.search(r'[¥￥]\s*([0-9]+(?:\.[0-9]{1,2})?)', raw_text)
        price = float(price_match.group(1)) if price_match else None

        # 寻找库存: 有货 · 3件 / 现货 3 / 库存 3
        stock_match = re.search(r'(?:有货|现货|库存)[^\d]{0,4}(\d+)\s*(?:件|个)?', raw_text)
        stock_count = int(stock_match.group(1)) if stock_match else None
        in_stock = (stock_count > 0) if stock_count is not None else ("有货" in raw_text)

        # 寻找质保与邮箱
        warranty_match = re.search(r'(质保[^\s,，。]+)', raw_text)
        warranty = warranty_match.group(1) if warranty_match else "未明确标注"

        email_feature = "含邮箱" if ("邮箱" in raw_text) else "未注明显式邮箱"

        return [{
            "name": f"{sku_kw} 对应规格",
            "real_price": price,
            "in_stock": in_stock,
            "stock_count": stock_count,
            "features": [email_feature, warranty],
            "notes": raw_text[:200] + "...",
            "source": "HTML_DOM_REGEX"
        }]
    return None


def verify_terminal(url, sku_kw=None):
    """主穿透验真函数"""
    print(f"[*] 正在穿透核验终端落地页: {url}", file=sys.stderr)
    res = fetch_url(url)

    if res["error"] and res["status_code"] == 0:
        return {
            "status": "error",
            "url": url,
            "message": f"连接失败: {res['error']}"
        }

    # 1. 检查 Cloudflare 拦截
    if check_cloudflare(res):
        return {
            "status": "cloudflare_challenge",
            "url": url,
            "message": "触发 Cloudflare 5秒盾/人机验证，需宿主浏览器 MCP 介入"
        }

    # 2. Level 1: 嗅探 REST API
    api_items = probe_rest_api(url, sku_kw)
    if api_items:
        return {
            "status": "verified",
            "url": url,
            "detection_method": "REST_API",
            "items": api_items
        }

    # 3. Level 2 & 3: 页面状态与 DOM 语义提取
    dom_items = probe_dom_regex(res["body"], sku_kw)
    if dom_items:
        return {
            "status": "verified",
            "url": url,
            "detection_method": "DOM_HEURISTICS",
            "items": dom_items
        }

    return {
        "status": "unverified",
        "url": url,
        "message": f"未能在落地页中自动识别出与 '{sku_kw or '通用'}' 相关的商品或价格规格"
    }


def main():
    parser = argparse.ArgumentParser(description="终端发卡落地页价格与库存穿透验真工具")
    parser.add_argument("url", help="待核验的目标店铺落地页 URL")
    parser.add_argument("--sku", "-s", default="", help="目标商品/规格关键词 (如: Muse, Claude, 成品号)")
    parser.add_argument("--json", "-j", action="store_true", help="以纯 JSON 格式输出结果")
    args = parser.parse_args()

    result = verify_terminal(args.url, args.sku)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    # 人性化控制台输出
    print("\n" + "=" * 55)
    print(f" 终端落地页核验报告: {result.get('url')}")
    print("=" * 55)
    status = result.get("status")
    print(f" 核验状态: {status}")

    if status == "verified":
        print(f" 识别技术: {result.get('detection_method')}\n")
        items = result.get("items", [])
        for idx, item in enumerate(items, 1):
            price_str = f"¥ {item['real_price']:.2f}" if item['real_price'] is not None else "未知"
            stock_str = f"{item['stock_count']} 件 (在售)" if item['stock_count'] is not None else ("有货" if item['in_stock'] else "缺货")
            print(f" [{idx}] 商品名称: {item['name']}")
            print(f"     实时单价: \033[32m{price_str}\033[0m")
            print(f"     实时库存: \033[33m{stock_str}\033[0m")
            if item.get("features"):
                print(f"     特性标签: {', '.join(str(f) for f in item['features'])}")
            if item.get("notes"):
                print(f"     质保须知: {item['notes']}")
            print("-" * 55)
    else:
        print(f" 结果提示: {result.get('message')}")
        print("=" * 55)


if __name__ == "__main__":
    main()
