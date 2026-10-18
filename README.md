# 2026 AI 发卡比价 & API 中转站精选指南

[简体中文](./README.md) | [English](./README_EN.md)

> 本项目通过自动化网络探针与多智能体独立审计，对主流第三方 AI 发卡聚合平台与 API 中转站进行实时采样测试与分类评级。纯技术实验与公开信息整理，零商业推广，无人工干预。
> 
> *An independent, multi-agent audited benchmark and curated directory for AI account subscriptions and developer API relays. Powered by automated terminal probes and deterministic decision gates.*

---

## 关于本项目 (About)

本项目全量收录并独立评测主流第三方 **AI 发卡聚合比价平台（16 家）** 与 **API 中转服务商（24 家）**，提供无商业推广的实时可用率监测与综合评级。

### 内置 Agent 智能体技能 (Built-in Skill)
项目内置专属智能体技能 **[`card-and-relay-tracker`](./.agents/skills/card-and-relay-tracker/SKILL.md)**。支持任意 AI 编程助手（Codex、Gemini、Claude、Cursor）直接调用，自动规避聚合站起步价刺客与过期货架缓存，实现**终端店铺真价穿透验真**，严格硬阻断“代认证/代充”混入成品号，直接交付带有效库存的购买直达链接。

> **English Summary**:
> An independent benchmark of 40 AI subscription platforms and API relays, featuring a built-in Agent Skill (`card-and-relay-tracker`) for real-time terminal price penetration, pure finished-account filtering, and direct purchasing URL delivery.

---

## 模块目录导航

| 模块 | 核心内容与评测重点 | 独立文档 |
| :--- | :--- | :---: |
| **卡网聚合比价榜** | ChatGPT、Claude、Gemini 订阅、成品号与兑换码比价（收录 16 家） | [`卡网完整榜`](./CARDS.md) |
| **API 中转站全量榜** | 开发者接口调用、真假官转鉴定、实时可用率测速与倍率换算（收录 24 家） | [`中转站全量榜`](./API_RELAY.md) |
| **多智能体打分体系** | 中立风控 (35%) + 数据功能 (35%) + 体验直连 (30%) 算法判据细则 | [`打分标准细则`](./SCORING.md) |
| **AI Agent 智能体技能** | 双阶段真价穿透、成品号一票否决门禁、7 维决策矩阵与 CLI 工具链 | [`智能体技能规约`](./.agents/skills/card-and-relay-tracker/SKILL.md) |
| **免责声明与使用条款** | 法律级非商业声明、资金安全严正警示及快速无条件移除流程 | [`免责声明条款`](./DISCLAIMER.md) |

---

## 精选推荐榜单 (T0 / T1)

### 一、卡网聚合比价

#### T0 推荐（综合得分 ≥ 88 分）

| 排名 | 得分 | 平台名称 | 官网链接 | 维度分 (中立/数据/体验) | 核心特性 |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **1** | **93.0** | **PriceAI** | [https://priceai.cc/](https://priceai.cc/) | 80 / 100 / 100 | 开源架构，现货库存与历史价格走势曲线完备，分类清晰，国内直连极速。 |
| **2** | **93.0** | **就爱比 (9AIB)** | [https://9aib.com/](https://9aib.com/) | 80 / 100 / 100 | 覆盖 350+ 验真店铺，具备现货底价雷达与真实性监控，模型品类极全。 |

#### T1 推荐（综合得分 78 ~ 87.9 分）

| 排名 | 得分 | 平台名称 | 官网链接 | 维度分 (中立/数据/体验) | 核心特性 |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **3** | **87.2** | **OpenPrice** | [https://www.openprice.cc/](https://www.openprice.cc/) | 85 / 100 / 75 | 开源比价，收录 280+ 渠道商，支持官方低价区汇率实时折算。 |
| **4** | **84.2** | **水獭比价** | [https://shuita.xyz/](https://shuita.xyz/) | 65 / 90 / 100 | 实时汇总 126 家发卡网现货，有货优先排序，页面清爽且响应极快。 |
| **5** | **82.0** | **AIFeeRadar** | [https://aifeeradar.com/](https://aifeeradar.com/) | 70 / 100 / 75 | 涵盖官方订阅、地区套餐与渠道报价多维横向对比。 |
| **6** | **81.8** | **Relay Radar** | [https://aicodex.chat/radar](https://aicodex.chat/radar) | 65 / 100 / 80 | 独立采集核验，明确标注有货最低价、渠道数与风险等级。 |
| **7** | **80.2** | **AIradar** | [https://airadar.vip/](https://airadar.vip/) | 70 / 90 / 80 | 提供订阅行情周报与降价提醒，卡片式交互体验良好。 |
| **8** | **80.2** | **比武 AI** | [https://biwu.ai/](https://biwu.ai/) | 70 / 90 / 80 | 监控 280+ 卡网价格，换算 42 个地区官方汇率。 |

[查阅全部 16 家卡网比价与 T2 备选列表](./CARDS.md)

---

### 二、API 中转站

#### T0 推荐（综合得分 ≥ 85 分）

| 排名 | 得分 | 平台名称 | 官网链接 | 维度分 (中立/数据/体验) | 核心特性 |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **1** | **90.0** | **RouterHubs** | [https://routerhubs.com/](https://routerhubs.com/) | 80 / 100 / 90 | 不抽成、不代理，24 家中转可用率、延迟与价格独立快照。 |
| **2** | **87.2** | **TokenAPI Scan** | [https://tokenscanai.com/](https://tokenscanai.com/) | 85 / 100 / 75 | 监测 391 家中转红黑榜，专项测试假官转与逆向高仿。 |
| **3** | **87.0** | **EggStriker** | [https://www.eggstriker.com/ai-api](https://www.eggstriker.com/ai-api) | 80 / 100 / 80 | 144 家中转全景对比，涵盖直连测速、模型价格与倍率换算。 |
| **4** | **86.5** | **APITokenNav** | [https://apitokennav.com/](https://apitokennav.com/) | 70 / 100 / 90 | 收录 105 个中转，支持按客户端（Cursor/Codex）与充值门槛筛选。 |
| **5** | **85.0** | **API Ranking** | [https://apiranking.com/](https://apiranking.com/) | 70 / 100 / 85 | 持续跟踪各中转最新换绑网址，提供多模型对比榜。 |

#### T1 推荐（综合得分 76 ~ 84.9 分）

| 排名 | 得分 | 平台名称 | 官网链接 | 维度分 (中立/数据/体验) | 核心特性 |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **6** | **84.8** | **zznav** | [https://zznav.site/](https://zznav.site/) | 65 / 100 / 90 | 包含跑路欺诈黑名单板块，国内直连极速。 |
| **7** | **84.8** | **禾维 AI** | [https://www.hvoyai.com/](https://www.hvoyai.com/) | 65 / 100 / 90 | 配套在线 API 鉴定器，输入 Key 与端点可实测 Claude/GPT 真假。 |
| **8** | **84.0** | **MODELOC** | [https://modeloc.com/relays](https://modeloc.com/relays) | 75 / 90 / 90 | 主打大模型原始一致性检测，收录中转目录并提供掺水审计与社区用户打分。 |
| **9** | **83.5** | **Veridrop (真伪榜)** | [https://veridrop.org/](https://veridrop.org/) | 80 / 90 / 80 | 业内权威真伪榜，站长授权 Key 持续检测模型纯度。 |
| **10** | **83.5** | **GetCheapAI** | [https://www.getcheapai.com/zh-cn](https://www.getcheapai.com/zh-cn) | 65 / 100 / 90 | 覆盖 60+ 中转与 520+ 模型，提供 90 分钟可用性与延迟探针，支持多币种折扣换算。 |
| **11** | **83.5** | **chatgpt.top** | [https://chatgpt.top/](https://chatgpt.top/) | 80 / 90 / 80 | 专为 Claude Code / Cursor / Codex 整理，全站无推广返利。 |
| **12** | **83.0** | **awesome-ai-api-proxy** | [https://howardpen9.github.io/awesome-ai-api-proxy/](https://howardpen9.github.io/awesome-ai-api-proxy/) | 85 / 75 / 90 | GitHub 开源项目，面向 AI Agent 的纯净价格观测端点。 |
| **13** | **81.8** | **Help AIO** | [https://www.helpaio.com/](https://www.helpaio.com/) | 75 / 90 / 80 | 自费实测购买，7×24 真实调用探针，公开口径杜绝作弊。 |
| **14** | **81.8** | **白嫖中转评测** | [https://baipiao.org/relay/](https://baipiao.org/relay/) | 65 / 90 / 85 | 14+ 站点真实请求测评，记录实际扣费与成功率。 |
| **15** | **81.2** | **OkkMax** | [https://www.okkmax.com/](https://www.okkmax.com/) | 60 / 90 / 85 | 提供纯度检测、上下文长度测试与“模型智商榜”。 |
| **16** | **80.2** | **ZZZNav** | [https://zzznav.com/](https://zzznav.com/) | 65 / 90 / 85 | 18 个模型官方牌价与 44 家中转倍率逐项折算。 |
| **17** | **80.2** | **API选** | [https://www.apixuan.com/](https://www.apixuan.com/) | 65 / 90 / 85 | 新手友好，提供精选推荐与常见客户端配置教程。 |
| **18** | **79.5** | **AI API 公益站** | [https://bubblevv.github.io/ai-api-gongyi-nav/](https://bubblevv.github.io/ai-api-gongyi-nav/) | 50 / 90 / 90 | GitHub 开源公益导航，收集免费额度与签到中转。 |
| **19** | **78.2** | **APIvs** | [https://apivs.si/](https://apivs.si/) | 65 / 90 / 85 | 基于真实请求测试可用率、首字延迟与协议兼容性。 |
| **20** | **76.5** | **纯度AI** | [https://chunduai.com/](https://chunduai.com/) | 70 / 80 / 80 | 整合编程工具教程，同步 Veridrop 检测榜单。 |
| **21** | **76.5** | **API搜** | [https://www.apisou.com/](https://www.apisou.com/) | 65 / 90 / 85 | 140+ 站点目录，按官转、开源、逆向标签分类。 |

[查阅全部 24 家中转站评测与 T2 备选列表](./API_RELAY.md)

---

## 评分体系摘要

```
综合得分 = 中立风控分 (35%) + 数据功能分 (35%) + 体验直连分 (30%)
```

- **中立与风控 (35%)**：审计开源透明度、真伪测试机制，排除隐藏推广返利外链与广告买榜。
- **数据与功能 (35%)**：自动化探针监测、现货库存实时同步、全模型覆盖与实时倍率折算。
- **体验与直连 (30%)**：国内网络免代理直连时延、现代化响应式排版、即时模糊搜索效率。

[查阅打分体系与权重细则](./SCORING.md)

---

## 安全须知与下架申请

1. **纯主观性与时效性**：本榜单为特定采样节点的技术快照，不构成消费、充值或商业投资建议。第三方站点更新频繁，不作稳定性担保。
2. **资金安全严正警示**：第三方服务跑路与封号风险极高，务必遵循“小额测试、按需充值、随用随走、切勿大额沉淀资金”原则。因使用第三方服务导致的任何纠纷或财产损失，本项目概不负责。
3. **无条件移除流程**：站点运营方如不希望被收录，请按照 [免责声明第八条](./DISCLAIMER.md#八异议沟通与侵权移除流程-notice-and-takedown) 提交 Issue，我们在核实后将尽快（通常 7 个工作日内）无条件彻底移除。

[查阅完整法律声明与使用条款](./DISCLAIMER.md)

---

## AI Agent 智能体协同与终端验真引擎 (AI Agent Skill & Terminal Verification Engine)

本项目不仅是人工查阅的静态名录，更是专为自主智能体（Codex、Gemini、Claude Code、Cursor 等）设计的结构化知识库与终端执行引擎。通过规范化契约与轻量化 Python 标准库工具，实现“**全量资产检索 + 落地店铺穿透验真 + 异常防御阻断**”的完整工程闭环。

### 一、双阶段穿透决策架构 (Two-Pass Penetration Architecture)

```
[用户指令 / 智能体意图识别]
           │
           ▼
┌────────────────────────────────────────┐
│  第一阶段：聚合层索引初筛 (Discovery)   │  ◄── targets.json (40 站点全量库)
│  - 广度匹配目标商品候选题录            │  ◄── GATE-01: 负向关键词一票否决
│  - 排除失效与历史无货渠道              │
└──────────────────┬─────────────────────┘
                   │ 提取候选店铺落地页 URL
                   ▼
┌────────────────────────────────────────┐
│  第二阶段：终端实时验真 (Penetration)   │  ◄── verify_terminal.py
│  - 防爬 / WAF 挑战盾识别与旁路复核     │
│  - DOM 邻近特征窗口防串价匹配          │
│  - 复合周期与折合月单价规范化计算      │
└──────────────────┬─────────────────────┘
                   │ 结构化真价数据 (real_price, in_stock > 0, direct_url)
                   ▼
┌────────────────────────────────────────┐
│  第三阶段：高信号决策卡片交付 (Output) │  ◄── 强制交付可点击落地购买直链
└────────────────────────────────────────┘
```

### 二、交互契约与智能体意图映射 (Interaction Contract Matrix)

智能体在解析用户自然语言请求时，遵循以下输入契约与执行管线：

| 意图模式 (Intent) | 契约输入范式 (Input Contract) | 智能体后台执行管线 (Execution Pipeline) |
| :--- | :--- | :--- |
| **成品号采购**<br>`Finished Account` | *"寻找 ChatGPT Plus 4 个月学生号成品，要求开箱即用，排除自备号代充"* | ① 加载 `spec_filters.finished_account.negative_keywords` 触发 GATE-01 硬阻断；<br>② 查询 T0/T1 聚合站锁定候选落地页；<br>③ 执行 `verify_terminal.py --require-tags "成品" --exclude-tags "代认证,自备"`；<br>④ 交付含购买直链与折合月单价卡片。 |
| **店铺实时真伪审计**<br>`Storefront Audit` | *"核验 https://buyai.dev/ 上 Muse 的实时库存与真实结算价"* | ① 执行 `verify_terminal.py "https://buyai.dev/" --sku "Muse" --json`；<br>② 探测 WAF 盾及 DOM 邻近价格，剔除已售罄底价；<br>③ 提取质保条款并在卡片中呈现。 |
| **中转站真伪与倍率审计**<br>`Relay Verification` | *"推荐两家真官转、不掺水且扣费倍率透明的 Claude 3.7 中转站"* | ① 查询 `targets.json` 的 `all_relay_directories`，筛选 T0 级基准站点；<br>② 执行 GATE-05 过滤纯度低于 80 分的站点；<br>③ 执行 GATE-06 统一换算每百万 Token 最终实付人民币价格。 |
| **全库外链存活巡检**<br>`Directory Sweeping` | *"执行全库外链健康探测与重定向换绑雷达追踪"* | ① 并发调度 `check_links.py --workers 10`；<br>② 捕获 301/302 跨域名跳转与服务下线，输出异常清单。 |

### 三、7 维机读判定门禁 (7-Dimensional Deterministic Decision Gates)

完整机读判据详见 [`references/anti_traps.md`](./.agents/skills/card-and-relay-tracker/references/anti_traps.md)：
- **GATE-01 (规格纯度)**：`FAIL`。命中“代认证/代充/自备号/包过”等词汇且诉求为成品时，一票否决。
- **GATE-02 (结算真价)**：`FAIL`。废弃聚合站缓存，强制采信落地页实时结算价，杜绝起步价刺客。
- **GATE-03 (有效库存)**：`FAIL`。排查幽灵秒发套路，库存为 0 或排队预售直接剔除。
- **GATE-04 (交付安全)**：`WARN`。自建企业邮警示高危，缺失独立邮箱直接降权。
- **GATE-05 (模型纯度)**：`FAIL`。MODELOC / Veridrop 纯度低于 80 分或存在降级行为直接阻断。
- **GATE-06 (倍率透明)**：`REQUIRED`。严禁采信宣传倍率，强制折算为每百万 Token 最终实付单价。
- **GATE-07 (上下文截断)**：`WARN`。长文本输入静默截断或逆向接口降级标记。

### 四、独立自动化 CLI 工具链 (Standalone CLI Toolchain)

除智能体自动调用外，开发者可在终端脱离 AI 直接执行纯 Python 标准库工具：

```bash
# 1. 发卡网落地页秒级真价穿透测试（支持防爬盾感知与标签强过滤）
python scripts/verify_terminal.py "https://buyai.dev/" --sku "Muse" --require-tags "成品" --exclude-tags "代认证,自备" --json

# 2. 全库 40+ 外链并发健康探测与跨域换绑雷达
python scripts/check_links.py --workers 10

# 支持代理分流网络环境
python scripts/check_links.py --proxy "http://127.0.0.1:7897"
```

---

## 社区勘误

若发现站点域名变更或状态失效，欢迎在 [Issues](https://github.com/waw666waw666/awesome-ai-relay-and-cards/issues) 提交反馈。
