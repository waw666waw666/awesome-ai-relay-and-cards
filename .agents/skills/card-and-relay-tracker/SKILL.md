---
name: card-and-relay-tracker
description: >
  AI 发卡店铺真实价格与库存穿透验真、API 中转站真伪鉴别及可用性巡检工具。
  全量内置收录 40 家卡网与 API 中转站（16 家卡网 + 24 家中转）。
  Use when the user asks to:
  - 查找、对比或核实 ChatGPT Plus/Pro、Claude Pro/Team、Gemini、Muse 等 AI 账号的真实在售渠道与现货价格；
  - 剔除发卡网起步价刺客、虚假库存、自备号代认证混淆等暗坑，提取真实结算价；
  - 鉴别 API 中转站真假官转、模型降级、倍率膨胀，或查询中转站可用性与健康度；
  - 对 awesome-ai-relay-and-cards 收录的全量 40 家站点进行健康探活与链接检测。
  Do NOT use for: 购买实体信用卡、黑灰产攻击或通用爬虫开发。
---

# card-and-relay-tracker 技能规约 (SOP)

本 Skill 为开源项目 [awesome-ai-relay-and-cards](https://github.com/waw666waw666/awesome-ai-relay-and-cards) 的专属比价验真与运维引擎。

---

## 一、内置资产库（全量 40 家站点索引）

本技能通过 `references/targets.json` **全量内置收录了全部 40 家评测站点**，无需重复解析 Markdown 即可毫秒级调用：
- **实时比价与探针靶标（6 家）**：`PriceAI`、`就爱比 (9AIB)`、`水獭比价`、`GetCheapAI`、`MODELOC`、`Veridrop`；
- **全量卡网聚合比价目录（16 家）**：涵盖 T0（PriceAI、9AIB）、T1（OpenPrice、水獭比价、AIFeeRadar 等 6 家）及 T2 备用目录；
- **全量 API 中转站评测目录（24 家）**：涵盖 T0（RouterHubs、TokenAPI Scan、EggStriker 等 5 家）、T1（zznav、禾维 AI、MODELOC 等 16 家）及 T2 备用目录；
- **标准 SKU 与规格过滤器**：内置 `finished_account` 与 `recharge_or_verify_service` 白黑名单，以及标准商品基准价池。

---

## 二、四大典型应用场景与操作路径

### 场景 1：找现货成品号 / 会员卡密（核心高频）
- **触发意图**：“找便宜的 ChatGPT 学生号成品”、“买 Claude Pro 独享号”、“哪家有 Gemini 现货/学生号”、“找 Cursor 账号”。
- **执行路径**：
  1. 直接运行内置全量聚合检索脚本：
     `python scripts/query_cards.py "<关键词>"`（如 `python scripts/query_cards.py "gemini"` 或 `python scripts/query_cards.py "chatgpt"`）；
  2. 脚本自动直连 T0 级聚合引擎 PriceAI 数据库（涵盖 50+ AI 品类与 1000+ 在售发卡店铺），并严格执行 GATE-01 ~ GATE-03 门禁规则，自动剔除“代充/代认证/自备号/人机验证/封号无售后”等陷阱；
  3. 输出通过门禁的实时在售店铺名、真实实付价、月折合单价、货品标题及直达购买链接；
  4. 如需对特定落地页进行单点深度 DOM 验真，执行 `python scripts/verify_terminal.py "<落地页URL>" --sku "<关键词>"`；
  5. 采用标准高信号卡片直接交付用户，拒绝长篇百科说教。

### 场景 2：查 API 中转站 / 鉴真假官转（模型开发者）
- **触发意图**：“推荐两家稳的 Claude 3.7 中转”、“查查某某中转靠不靠谱”、“有没有不掺水的中转”。
- **执行路径**：
  1. 读取 `targets.json` 的 `all_relay_directories`，按评分梯队推荐 T0 级中转（RouterHubs、TokenAPI Scan、EggStriker 等）；
  2. 调取 `anti_traps.md` 中的 GATE-05（纯度检测）、GATE-06（倍率膨胀换算）与 GATE-07（长上下文截断）；
  3. 强调实际每百万 Token 换算成本（`官方牌价 × 分组倍率 × 模型倍率`），提醒按需充值。

### 场景 3：单点落地页真伪与现货核实
- **触发意图**：“帮我看看这个发卡链接到底多少钱”、“这个链接有现货吗”。
- **执行路径**：
  1. 直接对用户提供的 URL 运行 `python scripts/verify_terminal.py "<URL>" --json`；
  2. 如遇 WAF 防护盾挑战（`status == waf_challenge`），协同宿主浏览器工具（playwright/chrome-devtools）复核并向用户汇报。

### 场景 4：全量站点健康度巡检与换绑预警
- **触发意图**：“全网巡检”、“检查所有外链有没有挂的”、“哪些域名换绑了”。
- **执行路径**：
  1. 运行 `python scripts/check_links.py --workers 10`；
  2. 检查输出中的 `[REDIRECT_CHANGED]` 状态，同步更新 `CARDS.md` 或 `API_RELAY.md`。

---

## 三、标准交付规范（拒绝说教）

向用户交付推荐结果时，**严格采用高信号卡片模板**，严禁在回复中输出长篇大论的免责说教：

| 发卡店铺 | 实时价格与时长 | 库存状态 | 交付规格 | 售后质保 | 购买直达链接 |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **微赞优品** | **¥ 140.00** (4个月，折合¥35/月) | 现货 15 件 | 学生已认证绑卡成品 (含原邮) | 首登质保 24 小时 | [点击直达购买](https://wzyp.cn/item/2kecki) |
| **CC大王** | **¥ 160.00** (4个月，折合¥40/月) | 现货 8 件 | 学生已认证绑卡成品 (含原邮) | 首登质保 | [点击直达购买](https://ccdawang.win/products/gptx) |

- **规格本质**：一句话说明供应链来源（如：海外高校 Edu 邮箱 + SheerID 学生优惠订阅 + 虚拟信用卡绑卡）；
- **核心避坑**：首登质保内务必测试可用性；及时绑定备用 2FA 并修改邮箱密码；请勿在账号内存放关键机密数据。

---

## 四、运维巡检与 Git 纪律

1. **外链巡检**：`python scripts/check_links.py`（支持宽容 SSL 与 Range 降级）。
2. **Git 提交准则**：
   - 仅在本地创建规范的中文 Commit（说明做什么、为什么做、如何验证）；
   - **严禁擅自执行 `git push`**，必须经用户明确授权后方可推送。
