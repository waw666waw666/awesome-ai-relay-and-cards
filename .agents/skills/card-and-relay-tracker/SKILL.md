---
name: card-and-relay-tracker
description: >
  AI 发卡店铺真实价格与库存穿透验真、API 中转站真伪鉴别及可用性巡检工具。
  Use when the user asks to:
  - 查找、对比或核实 ChatGPT Plus/Pro、Claude Pro/Team、Gemini、Muse 等 AI 账号的真实在售渠道与现货价格；
  - 剔除发卡网起步价刺客、虚假库存、自备号代认证混淆等暗坑，提取真实结算价；
  - 鉴别 API 中转站真假官转、模型降级、倍率膨胀，或巡检中转站可用性与健康度；
  - 对 awesome-ai-relay-and-cards 收录的站点进行健康探活与链接检测。
  Do NOT use for: 购买实体信用卡、黑灰产攻击或通用爬虫开发。
---

# card-and-relay-tracker 技能规约 (SOP)

本 Skill 为开源项目 [awesome-ai-relay-and-cards](https://github.com/waw666waw666/awesome-ai-relay-and-cards) 的专属比价验真与运维引擎。

---

## 核心原则：两阶段穿透验真 (Two-Pass Verification)

- **第一阶段（寻路初筛）**：比价站数据仅作为发现候选店铺落地页的“导航索引”，其标价不可直接向用户汇报。
- **第二阶段（穿透验真）**：针对候选店铺落地页执行 `verify_terminal.py`，提取实时结算价、真实库存（>0）及规格属性。未经验真的价格严禁采信。

---

## 执行流程 SOP 四步法

### Step 1：意图解析与标签锁定
1. 提取目标商品与规格属性：
   - **成品号**：必须为商家预先注册、已绑卡或已开通订阅、附带账号+密码+邮箱资料的商品。
   - **代充/代认证**：买家自备账号的辅助服务。
2. **门禁规则**：用户明确需要“成品/成品号”时，自动加载 `references/targets.json` 中的 `spec_filters.finished_account.negative_keywords`，对所有候选实施一票否决。

### Step 2：聚合层一票否决初筛
1. 检索 `references/targets.json` 中的 T0/T1 聚合站（PriceAI、水獭比价、9AIB）：
   - 过滤所有命中负向词（“代认证”、“自备号”、“单认证”、“包过”）的条目；
   - 筛选出 2~4 家标称有货的最终购买落地页 URL。

### Step 3：落地页穿透验真与防爬处理
1. 在项目根目录下执行轻量验真脚本：
   ```bash
   python scripts/verify_terminal.py "<落地页URL>" --sku "<关键词>" --require-tags "成品" --exclude-tags "代认证,自备,代充" --json
   ```
2. 状态判定与处置：
   - `status == "verified"`：确认为真实在售现货，记录 `real_price`、`stock_count`、`duration` 及质保信息；
   - `status == "waf_challenge"`：触发 Cloudflare 或国内 WAF 挑战，调用宿主浏览器工具（playwright/chrome-devtools）复核，或在结果中标注 `[需手动核验实价]`；
   - `status == "spec_rejected"` 或 `unverified`：不满足成品规格或缺货，直接剔除该候选。

### Step 4：高信号决策卡片交付
交付内容仅包含：**方案对比表格**、**供应链本质说明**、**3项极简实操要点**。拒绝任何冗长说教。

#### 交付示例模板：
| 发卡店铺 | 实时价格与时长 | 库存状态 | 交付规格 | 售后质保 | 购买直达链接 |
| :--- | :---: | :---: | :--- | :--- | :--- |
| **微赞优品** | **¥ 140.00** (4个月，折合¥35/月) | 现货 15 件 | 学生已认证绑卡成品 (含原邮) | 首登质保 24 小时 | [点击直达购买](https://wzyp.cn/item/2kecki) |
| **CC大王** | **¥ 160.00** (4个月，折合¥40/月) | 现货 8 件 | 学生已认证绑卡成品 (含原邮) | 首登质保 | [点击直达购买](https://ccdawang.win/products/gptx) |

- **规格本质**：海外高校 Edu 邮箱 + SheerID 学生优惠订阅 + 虚拟信用卡绑卡扣款；
- **核心避坑**：首登质保内务必测试可用性；及时绑定备用 2FA 并修改邮箱密码；请勿在账号内存放关键机密数据。

---

## 运维巡检与 Git 纪律

### 外链巡检命令
```bash
python scripts/check_links.py
```

### Git 提交准则
- 仅在本地创建规范的中文 Commit（说明做什么、为什么做、如何验证）；
- **严禁擅自执行 `git push`**，必须经用户明确授权后方可推送。
