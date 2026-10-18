---
name: card-and-relay-tracker
description: >
  AI 发卡店铺真实价格与库存穿透验真、API 中转站真伪鉴别及可用性巡检工具。
  Use when the user asks to:
  - 查找、对比或核实 ChatGPT Plus/Pro、Claude Pro/Team、Gemini、Muse 等 AI 账号或充值的真实在售渠道与现货价格；
  - 揭穿发卡网“起步价套路、虚假库存、隐藏手续费、自建高危邮箱、严苛售后”等暗坑；
  - 鉴别 API 中转站真假官转、模型掺水降级、倍率双重膨胀，或排查中转站可用性与健康度；
  - 对 awesome-ai-relay-and-cards 收录的 40+ 站点进行自动化健康探活与失效链接检测。
  Do NOT use for: 购买实体信用卡、黑灰产盗号攻击或通用爬虫开发。
---

# card-and-relay-tracker 技能说明与操作规范

本 Skill 为开源项目 [awesome-ai-relay-and-cards](https://github.com/waw666waw666/awesome-ai-relay-and-cards) 的专属自动化运维与多源比价引擎。

---

## 核心纪律：两阶段穿透验真原则 (Two-Pass Verification)

**【铁律】绝对禁止直接将比价聚合网站（如水獭、PriceAI）的历史缓存底价作为最终真实售价汇报给用户！**

1. **第一阶段：广度寻源（Discovery Phase）**
   - 检索项目收录的 `CARDS.md`、`API_RELAY.md` 或调用 `references/targets.json` 中的比价端点，快速筛选出 3~5 家标有名义现货的候选发卡店铺落地页 URL。
2. **第二阶段：深度穿透验真（Verification Phase）**
   - 针对候选店铺落地页，执行项目内置的轻量验真脚本：
     ```bash
     python scripts/verify_terminal.py <落地页URL> --sku <目标规格关键词>
     ```
   - 脚本必须直通终端店铺，精准提取**实时结算标价、实时在售库存（>0）、交付规格及质保条款**。
   - 只有经过二阶段核验真实有货的店铺，才允许排入最终推荐清单。
   - 若遇到店铺 Cloudflare 5 秒盾无法脚本直连，应如实标注 `[需人工核实实付价]` 或通过宿主浏览器工具协同复核，严禁主观编造或延用聚合站过期缓存。

---

## 标准执行流程（SOP 四步法）

### Step 1：需求规格归一
- 明确用户目标：
  - 目标商品：如 `Muse AI`、`Claude Pro 独享号`、`10亿 Token 扩容码`；
  - 规格偏好：是需要`成品号（含一手邮箱）`还是只需要`激活码/代充`；
  - 约束条件：现货优先、单价底价、是否支持国内直连与支付宝/微信支付。

### Step 2：靶标索引初筛
- 查阅 `references/targets.json` 中的靶标列表：
  - 找成品号/激活码 -> 优先检索 `PriceAI`、`水獭比价`、`就爱比 (9AIB)` 等；
  - 找 API 价格/测速 -> 优先检索 `GetCheapAI`、`EggStriker`；
  - 鉴别真伪/防掺水 -> 优先检索 `MODELOC`、`Veridrop`。

### Step 3：终端店铺穿透核验
- 对初筛出的具体购买落地页（如 `https://buyai.dev/`），运行终端验真：
  ```bash
  # 项目根目录下运行，或直接使用绝对路径：
  python scripts/verify_terminal.py "https://buyai.dev/" --sku "Muse"
  ```
- 确认返回值中 `in_stock == true` 且 `real_price` 为真实联动后价格，彻底过滤掉“起步价刺客”与“幽灵无货”店铺。

### Step 4：人性化决策卡片与购买直链交付（强制规则）

**【交付铁律】**
1. **必须提供真实购买落地页链接**：每一家推荐店铺必须附带直接可点击的购买链接（如 `https://wzyp.cn/item/...`），严禁只给平台大门或只说数字。
2. **多月/复合规格清晰折算**：对于特殊周期商品（如 4 个月学生号、季度号、Token 包），必须同时标明**总价与月折合单价**（例如：`¥ 140.00 (4个月，折合 ¥35/月)`），严禁将总价误读为单月。
3. **拒绝说教式免责，只给精炼实操建议**：摒弃长篇大论背诵，按以下格式极简交付：
   - **方案表格**（店铺名、实测价格与周期、在售库存、购买直达链接）；
   - **规格本质说明**（一句话讲清该商品的供应链本质）；
   - **3 点核心避坑**（首登质保、密码/2FA 更改、重要数据隔离）。

```markdown
| 发卡店铺 | 实时价格与时长 | 库存状态 | 规格说明 | 质保售后 | 购买直达链接 |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **微赞优品** | **¥ 140.00** (4个月，折合¥35/月) | 有货 | 学生认证已绑卡成品 | 首登质保 | [点击直达购买](https://wzyp.cn/item/2kecki) |
| **CC大王** | **¥ 160.00** (4个月，折合¥40/月) | 库存 12 件 | 学生认证已绑卡成品 | 首登质保 | [点击直达购买](https://ccdawang.win/products/gptx) |
```

---

## 仓库链接健康巡检 SOP

当需要对收录的所有 40+ 卡网与中转站进行健康检查时：
```bash
# 执行全量并发探活（HEAD 优先，平滑回退 GET 1KB）
python scripts/check_links.py

# 如需同时测试代理分流
python scripts/check_links.py --proxy "http://127.0.0.1:7897"
```
脚本将输出状态表格与 `[REDIRECT_DOMAIN_CHANGE]` 域名换绑告警，根据输出结果直接更新 `CARDS.md` 或 `API_RELAY.md`。

---

## Git 提交纪律规范
1. 完成技能、脚本或数据更新后，仅在本地创建规范的中文 Git Commit。
2. **严禁擅自执行 `git push`**；必须在对话中向用户明确展示待推送的分支与 commit 摘要，取得用户显式确认授权后方可执行推送。
