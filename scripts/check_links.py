#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_links.py - 仓库全量卡网与中转站链接健康度巡检脚本
自动化提取项目 Markdown 文件中的所有外部站点链接，采用 HEAD 优先 + GET 1KB 平滑回退机制并发探测，
并追踪跨域名重定向（换绑雷达）。纯 Python 标准库实现。
"""

import sys
import os
import re
import json
import time
import argparse
import urllib.request
import urllib.error
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)


def extract_urls_from_markdown(file_paths):
    """从 Markdown 文件中提取所有 HTTP/HTTPS 外链"""
    urls = set()
    # 匹配 Markdown 标准链接 [text](url) 以及标准裸 URL
    md_link_pattern = re.compile(r'\[.*?\]\((https?://[^)\s]+)\)')
    bare_url_pattern = re.compile(r'https?://[a-zA-Z0-9\-._~:/?#@!$&*+,;%=]+')
    
    for path in file_paths:
        if not os.path.exists(path):
            continue
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                # 优先提取 markdown 中的括号链接
                for u in md_link_pattern.findall(content):
                    cleaned = u.strip().rstrip(").,;'\"")
                    parsed = urlparse(cleaned)
                    if parsed.netloc and "github.com/waw666waw666" not in cleaned:
                        urls.add(cleaned)
                # 再提取裸 URL
                for m in bare_url_pattern.findall(content):
                    cleaned = m.strip().rstrip(").,;'\"")
                    parsed = urlparse(cleaned)
                    if parsed.netloc and "github.com/waw666waw666" not in cleaned:
                        urls.add(cleaned)
        except Exception as e:
            print(f"[!] 读取 {path} 出错: {e}", file=sys.stderr)
            
    return sorted(list(urls))


def probe_single_url(url, proxy=None, timeout=6):
    """双阶平滑探测单个 URL (HEAD -> GET 1KB)"""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "*/*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }
    
    opener = urllib.request.build_opener()
    if proxy:
        opener.add_handler(urllib.request.ProxyHandler({"http": proxy, "https": proxy}))

    start_time = time.time()
    initial_domain = urlparse(url).netloc.lower()

    # 第一阶: 轻量 HEAD 请求
    try:
        req = urllib.request.Request(url, headers=headers, method="HEAD")
        with opener.open(req, timeout=timeout) as resp:
            elapsed_ms = int((time.time() - start_time) * 1000)
            final_url = resp.geturl()
            final_domain = urlparse(final_url).netloc.lower()
            redirect_changed = (initial_domain != final_domain) and (initial_domain.replace("www.", "") != final_domain.replace("www.", ""))
            
            return {
                "url": url,
                "status_code": resp.status,
                "latency_ms": elapsed_ms,
                "final_url": final_url,
                "redirect_changed": redirect_changed,
                "state": "REDIRECT_CHANGED" if redirect_changed else "OK",
                "method": "HEAD",
                "error": None
            }
    except (urllib.error.HTTPError, urllib.error.URLError, Exception) as e:
        # 如果是 403, 405 或其它异常，平滑降级到第二阶 GET
        pass

    # 第二阶: GET 请求 (Range 1KB)
    get_headers = dict(headers)
    get_headers["Range"] = "bytes=0-1024"
    try:
        req = urllib.request.Request(url, headers=get_headers, method="GET")
        with opener.open(req, timeout=timeout) as resp:
            elapsed_ms = int((time.time() - start_time) * 1000)
            final_url = resp.geturl()
            final_domain = urlparse(final_url).netloc.lower()
            redirect_changed = (initial_domain != final_domain) and (initial_domain.replace("www.", "") != final_domain.replace("www.", ""))

            return {
                "url": url,
                "status_code": resp.status,
                "latency_ms": elapsed_ms,
                "final_url": final_url,
                "redirect_changed": redirect_changed,
                "state": "REDIRECT_CHANGED" if redirect_changed else "OK",
                "method": "GET_RANGE",
                "error": None
            }
    except urllib.error.HTTPError as e:
        elapsed_ms = int((time.time() - start_time) * 1000)
        return {
            "url": url,
            "status_code": e.code,
            "latency_ms": elapsed_ms,
            "final_url": url,
            "redirect_changed": False,
            "state": "FAIL" if e.code in (404, 502, 503) else "WARN",
            "method": "GET_FAIL",
            "error": f"HTTP {e.code}"
        }
    except Exception as e:
        elapsed_ms = int((time.time() - start_time) * 1000)
        return {
            "url": url,
            "status_code": 0,
            "latency_ms": elapsed_ms,
            "final_url": url,
            "redirect_changed": False,
            "state": "DEAD",
            "method": "ERROR",
            "error": str(e)
        }


def check_all_links(urls, proxy=None, max_workers=10):
    """并发巡检全部链接"""
    print(f"[*] 启动并发健康巡检，待探测外链总数: {len(urls)} 条...", file=sys.stderr)
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(probe_single_url, u, proxy): u for u in urls}
        for future in as_completed(futures):
            res = future.result()
            results.append(res)
            # 实时进度打点
            state_flag = "+" if res["state"] == "OK" else ("!" if "REDIRECT" in res["state"] else "x")
            print(f" [{state_flag}] {res['state']:<16} {res['latency_ms']:>4}ms | {res['url']}", file=sys.stderr)

    return sorted(results, key=lambda x: (0 if x["state"] == "OK" else (1 if "REDIRECT" in x["state"] else 2), x["url"]))


def main():
    parser = argparse.ArgumentParser(description="全量收录卡网与中转站链接健康度巡检工具")
    parser.add_argument("--files", "-f", nargs="+", default=["CARDS.md", "API_RELAY.md", "README.md"], help="待扫描的 Markdown 文件")
    parser.add_argument("--proxy", "-p", default=None, help="代理服务器地址 (如: http://127.0.0.1:7897)")
    parser.add_argument("--json", "-j", action="store_true", help="以 JSON 格式输出结果")
    parser.add_argument("--workers", "-w", type=int, default=10, help="并发线程数 (默认 10)")
    args = parser.parse_args()

    # 切换到项目根目录
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_files = [os.path.join(repo_dir, f) if not os.path.isabs(f) else f for f in args.files]

    urls = extract_urls_from_markdown(target_files)
    if not urls:
        print("[!] 未在指定文件中提取到有效外链", file=sys.stderr)
        return

    results = check_all_links(urls, proxy=args.proxy, max_workers=args.workers)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    # 终端摘要看板
    print("\n" + "=" * 80)
    print(" 链接巡检与换绑雷达看板 (Link Health & Redirect Radar)")
    print("=" * 80)

    ok_count = sum(1 for r in results if r["state"] == "OK")
    redir_count = sum(1 for r in results if r["state"] == "REDIRECT_CHANGED")
    fail_count = sum(1 for r in results if r["state"] in ("FAIL", "DEAD"))

    print(f" 总检测量: {len(results)} | 正常: {ok_count} | 换绑/重定向: {redir_count} | 异常/失效: {fail_count}\n")

    if redir_count > 0:
        print(" [!] 跨域名换绑预警 (建议更新 Markdown 文档中的链接):")
        for r in results:
            if r["state"] == "REDIRECT_CHANGED":
                print(f"     原链接: {r['url']}")
                print(f"     -> 新链接: {r['final_url']}")
        print("-" * 80)

    if fail_count > 0:
        print(" [X] 访问异常或失效站点:")
        for r in results:
            if r["state"] in ("FAIL", "DEAD"):
                print(f"     {r['url']} (原因: {r['error']})")
        print("-" * 80)

    print("=" * 80)


if __name__ == "__main__":
    main()
