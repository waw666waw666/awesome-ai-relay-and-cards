# AI 发卡比价与 API 中转站精选指南 (2026)

> 本项目通过自动化网络探针与多智能体独立审计，对主流第三方 AI 发卡聚合平台与 API 中转站进行实时采样测试与分类评级。纯技术实验与公开信息整理，零商业推广，无人工干预。

---

## 模块目录导航

| 模块 | 核心内容与评测重点 | 独立文档 |
| :--- | :--- | :---: |
| **卡网聚合比价榜** | ChatGPT、Claude、Gemini 订阅、成品号与兑换码比价（收录 16 家） | [`卡网完整榜`](./CARDS.md) |
| **API 中转站全量榜** | 开发者接口调用、真假官转鉴定、实时可用率测速与倍率换算（收录 24 家） | [`中转站全量榜`](./API_RELAY.md) |
| **多智能体打分体系** | 中立风控 (35%) + 数据功能 (35%) + 体验直连 (30%) 算法判据细则 | [`打分标准细则`](./SCORING.md) |
| **Agent 维护技能** | 终端发卡落地页两段式穿透验真规范、14 维避坑手册与自动化工具 | [`智能体技能`](./.agents/skills/card-and-relay-tracker/SKILL.md) |
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

## Agent 维护技能与自动化工具

本项目内置开箱即用的 AI 智能体技能规范与轻量化纯 Python 校验工具，确保价格检索与外链状态不依赖聚合站过期货架缓存：

- **专属 Agent Skill**: [`.agents/skills/card-and-relay-tracker/SKILL.md`](./.agents/skills/card-and-relay-tracker/SKILL.md)
  - 规范 AI 智能体在面对比价和找号请求时的执行流程：严禁直信聚合站缓存标价，强制两段式穿透到终端发卡落地页。
  - 涵盖 14 维发卡网与中转站实战避坑手册（[`anti_traps.md`](./.agents/skills/card-and-relay-tracker/references/anti_traps.md)）及精选站点嗅探靶标注册表（[`targets.json`](./.agents/skills/card-and-relay-tracker/references/targets.json)）。
- **落地页真价穿透验真脚本**: [`scripts/verify_terminal.py`](./scripts/verify_terminal.py)
  - 纯 Python 标准库实现，支持自动嗅探发卡网开放 REST API / 提取页面状态 JSON，精准穿透 SKU 下拉选项，捕获真实在售价格、当前库存与售后质保条款。
  - 使用示例：
    ```bash
    python scripts/verify_terminal.py --url "https://buyai.dev/" --sku "Muse"
    ```
- **全量外链探活与换绑追踪脚本**: [`scripts/check_links.py`](./scripts/check_links.py)
  - 并发执行 HEAD 探测 + GET 1KB 范围平滑回退，自动追踪跨域名 301/302 重定向换绑与下线预警。
  - 使用示例：
    ```bash
    python scripts/check_links.py --workers 10
    ```

---

## 社区勘误

若发现站点域名变更或状态失效，欢迎在 [Issues](https://github.com/waw666waw666/awesome-ai-relay-and-cards/issues) 提交反馈。
