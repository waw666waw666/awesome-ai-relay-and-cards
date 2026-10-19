#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
query_cards.py - AI 发卡商品全量聚合查询与门禁过滤引擎
基于开源聚合平台 PriceAI 全量实时数据库（50+ AI 产品品类，实时汇总 1000+ 在售发卡店铺），
实现从“关键词意图识别 -> 匹配产品品类 -> 抓取实时在售店铺列表 -> 自动化门禁过滤 (GATE-01~04) -> 结构化高信号交付”。
纯 Python 标准库实现，零第三方依赖。
"""

import sys
import os
import re
import ssl
import json
import time
import argparse
import urllib.request
import urllib.error

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

DEFAULT_NEGATIVES = [
    "代充", "代开", "代认证", "包过", "自备", "需自备",
    "提供账号", "拍下发账号", "扫码登录", "只包认证", "不含订阅",
    "不是成品", "人机验证", "封号无售后", "申诉无售后"
]

CACHE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".priceai_channels_cache.json")
CACHE_TTL = 900  # 15 分钟缓存


def get_ssl_context():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def fetch_url(url, timeout=10):
    headers = {"User-Agent": USER_AGENT}
    req = urllib.request.Request(url, headers=headers)
    ctx = get_ssl_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def reconstruct_rsc(html):
    """从 Next.js App Router 响应中重组 RSC (self.__next_f.push) 数据流"""
    raw_chunks = re.findall(r'self\.__next_f\.push\(\[1,\s*\"((?:[^\"\\]|\\.)*)\"\]\)', html)
    full_text = ""
    for c in raw_chunks:
        try:
            full_text += json.loads('"' + c + '"')
        except Exception:
            full_text += c.replace('\\"', '"').replace('\\\\', '\\').replace('\\n', '\n')
    return full_text


def get_all_products(force_refresh=False):
    """获取 PriceAI 全量 53+ AI 产品品类及行情概览（带本地缓存）"""
    now = time.time()
    if not force_refresh and os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                cached = json.load(f)
                if now - cached.get("timestamp", 0) < CACHE_TTL:
                    return cached.get("products", [])
        except Exception:
            pass

    try:
        html = fetch_url("https://priceai.cc/channels", timeout=12)
        rsc = reconstruct_rsc(html)
        pos = rsc.find('"products":')
        if pos == -1:
            return []
        start_idx = rsc.find('[', pos)
        count = 0
        end_idx = start_idx
        for i in range(start_idx, len(rsc)):
            if rsc[i] == '[': count += 1
            elif rsc[i] == ']':
                count -= 1
                if count == 0:
                    end_idx = i + 1
                    break
        products = json.loads(rsc[start_idx:end_idx])
        # 写入缓存
        try:
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump({"timestamp": now, "products": products}, f, ensure_ascii=False)
        except Exception:
            pass
        return products
    except Exception as e:
        sys.stderr.write(f"[*] 抓取全量品类库失败: {e}\n")
        return []


def fetch_product_offers(slug):
    """获取某个指定品类（slug）在全网所有发卡店铺的实时挂单列表"""
    url = f"https://priceai.cc/products/{slug}"
    try:
        html = fetch_url(url, timeout=12)
        rsc = reconstruct_rsc(html)
        pos = rsc.find('"offers":')
        if pos == -1:
            return []
        start_idx = rsc.find('[', pos)
        count = 0
        for i in range(start_idx, len(rsc)):
            if rsc[i] == '[': count += 1
            elif rsc[i] == ']':
                count -= 1
                if count == 0:
                    return json.loads(rsc[start_idx:i+1])
        return []
    except Exception as e:
        sys.stderr.write(f"[*] 抓取商品 {slug} 在售报价失败: {e}\n")
        return []


def match_products(keyword, products):
    """基于关键词模糊匹配对应的 Product Slug 列表"""
    kw = keyword.lower().strip()
    matched = []

    # 常见别名映射表加速
    KEYWORD_ALIASES = {
        "gemini": ["gemini-pro-year", "gemini-pro-recharge", "gemini-ultra-5x", "gemini-ultra"],
        "google": ["gemini-pro-year", "gmail-account", "google-phone-verification"],
        "chatgpt": ["chatgpt-plus", "chatgpt-free-account", "chatgpt-pro-20x", "chatgpt-team-business"],
        "gpt": ["chatgpt-plus", "chatgpt-free-account", "chatgpt-pro-20x"],
        "claude": ["claude-pro-month", "claude-account", "claude-max-20x", "claude-team-standard"],
        "cursor": ["cursor-account"],
        "grok": ["super-grok", "super-grok-lite", "grok-super", "grok-account"],
        "edu": ["education-email"],
        "学生": ["education-email", "gemini-pro-year", "chatgpt-plus"],
        "邮箱": ["gmail-account", "outlook-account", "education-email", "icloud-email"]
    }

    alias_matches = set()
    for k, slugs in KEYWORD_ALIASES.items():
        if k in kw or kw in k:
            alias_matches.update(slugs)

    for p in products:
        slug = p.get("slug", "")
        name = p.get("displayName", "")
        platform = p.get("platform", "")
        aliases = p.get("aliases", [])
        summary = p.get("summary", "")

        is_match = False
        if slug in alias_matches:
            is_match = True
        elif kw in slug.lower() or kw in name.lower() or kw in platform.lower():
            is_match = True
        elif any(kw in a.lower() for a in aliases):
            is_match = True

        if is_match:
            matched.append(p)

    return matched


def filter_offers(offers, exclude_tags=None, require_finished=True):
    """执行 GATE-01 ~ GATE-03 门禁规则过滤"""
    negatives = list(DEFAULT_NEGATIVES)
    if exclude_tags:
        negatives.extend(exclude_tags)

    filtered = []
    for o in offers:
        if o.get("status") != "in_stock":
            continue

        title = o.get("sourceTitle", "")
        # GATE-01: 负向黑名单一票否决
        if any(neg in title for neg in negatives):
            continue

        # 检查是否自备号或非成品
        if require_finished:
            if "代" in title and "成品" not in title:
                continue

        filtered.append(o)

    # 按价格由低到高排序
    filtered.sort(key=lambda x: float(x.get("price") or 999999))
    return filtered


def parse_duration_and_unit_price(title, price):
    """智能解析时长并计算月折合单价"""
    m = re.search(r'(\d+)\s*(?:个)?月', title)
    if m:
        months = int(m.group(1))
        if months > 0:
            unit = round(price / months, 2)
            return f"{months}个月", f"约¥{unit}/月"

    if "一年" in title or "1年" in title or "12个月" in title or "年卡" in title:
        unit = round(price / 12, 2)
        return "12个月", f"约¥{unit}/月"

    if "季度" in title or "季卡" in title or "3个月" in title:
        unit = round(price / 3, 2)
        return "3个月", f"约¥{unit}/月"

    return "按需/单次", f"¥{price}"


def main():
    parser = argparse.ArgumentParser(description="AI 发卡商品全量聚合查询与门禁过滤引擎")
    parser.add_argument("keyword", nargs="?", default="", help="搜索关键词（如 gemini, chatgpt, claude, cursor 等）")
    parser.add_argument("--slug", help="直接查询指定产品 Slug（如 gemini-pro-year）")
    parser.add_argument("--limit", type=int, default=5, help="每个品类输出在售店铺数量上限（默认 5）")
    parser.add_argument("--exclude-tags", help="自定义额外负向阻断关键词（逗号分隔）")
    parser.add_argument("--no-filter", action="store_true", help="关闭自动门禁过滤（查看全部原始挂单）")
    parser.add_argument("--refresh", action="store_true", help="强制刷新本地品类缓存")
    parser.add_argument("--json", action="store_true", help="以 JSON 格式输出结果")

    args = parser.parse_args()

    if not args.keyword and not args.slug:
        parser.print_help()
        sys.exit(1)

    exclude_tags = [t.strip() for t in args.exclude_tags.split(",")] if args.exclude_tags else []

    products = get_all_products(force_refresh=args.refresh)
    if not products:
        if args.json:
            print(json.dumps({"status": "error", "message": "无法连接至聚合平台获取品类数据"}, ensure_ascii=False))
        else:
            print("[!] 获取品类数据失败，请检查网络连接。")
        sys.exit(1)

    target_products = []
    if args.slug:
        target_products = [p for p in products if p.get("slug") == args.slug]
    else:
        target_products = match_products(args.keyword, products)

    if not target_products:
        if args.json:
            print(json.dumps({"status": "not_found", "message": f"未找到与 '{args.keyword}' 匹配的 AI 产品品类"}, ensure_ascii=False))
        else:
            print(f"[!] 未找到与 '{args.keyword}' 匹配的 AI 产品品类。")
        sys.exit(0)

    results = []

    for p in target_products:
        slug = p.get("slug")
        name = p.get("displayName")
        platform = p.get("platform")
        lowest_price = p.get("lowestPrice")
        in_stock_count = p.get("inStockCount")

        raw_offers = fetch_product_offers(slug)
        if args.no_filter:
            final_offers = raw_offers
        else:
            final_offers = filter_offers(raw_offers, exclude_tags=exclude_tags)

        # 截取 limit
        sliced_offers = final_offers[:args.limit]

        formatted_offers = []
        for o in sliced_offers:
            price = float(o.get("price") or 0)
            title = o.get("sourceTitle", "")
            duration, unit_price = parse_duration_and_unit_price(title, price)

            formatted_offers.append({
                "store_name": o.get("sourceStoreName", "未知店铺"),
                "price": price,
                "duration": duration,
                "unit_price": unit_price,
                "title": title,
                "url": o.get("url", ""),
                "status": o.get("status", "")
            })

        results.append({
            "platform": platform,
            "product_name": name,
            "slug": slug,
            "total_in_stock_merchants": in_stock_count,
            "passed_gate_merchants": len(final_offers),
            "offers": formatted_offers
        })

    if args.json:
        print(json.dumps({"status": "success", "keyword": args.keyword, "results": results}, ensure_ascii=False, indent=2))
        return

    # 输出人类友好高信号 Markdown 表格
    for res in results:
        print(f"\n### 📦 【{res['platform']}】{res['product_name']} (在售商户: {res['total_in_stock_merchants']} 家 | 门禁通过: {res['passed_gate_merchants']} 家)")
        if not res["offers"]:
            print("> 当前无符合纯度门禁（已排除代认证/代充/封号风险）的现货店铺。\n")
            continue

        print("| 发卡店铺 | 实时价格与时长 | 月折算单价 | 货品标题与规格 | 购买直达链接 |")
        print("| :--- | :---: | :---: | :--- | :--- |")
        for o in res["offers"]:
            clean_title = o["title"].replace("|", " ").strip()
            if len(clean_title) > 38:
                clean_title = clean_title[:35] + "..."
            print(f"| **{o['store_name']}** | **¥ {o['price']:.2f}** ({o['duration']}) | {o['unit_price']} | {clean_title} | [点击直达购买]({o['url']}) |")


if __name__ == "__main__":
    main()
