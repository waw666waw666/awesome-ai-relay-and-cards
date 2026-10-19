# 2026 AI Subscription Pricing & API Relay Curated Guide

[English](./README_EN.md) | [简体中文](./README.md)

> An independent benchmark covering **16 AI subscription aggregators** and **24 developer API relays** with zero commercial bias.
> 
> **Built-in AI Procurement Secretary**: Features the **[`card-and-relay-tracker`](./.agents/skills/card-and-relay-tracker/SKILL.md)** skill for autonomous coding agents (Codex, Gemini, Claude, Cursor) to act as an executive procurement secretary—identifying genuine intent, filtering degraded or ban-risk accounts across 1000+ merchant stores, and presenting executive purchase briefs with direct clickable links.

---

## Directory Navigation

| Module | Core Scope & Evaluation Focus | Document Link |
| :--- | :--- | :---: |
| **Card & Account Aggregators** | ChatGPT, Claude, Gemini subscriptions, finished accounts & redemption codes (16 platforms) | [`CARDS.md`](./CARDS.md) |
| **API Relay Benchmarks** | Developer API endpoints, authenticity audits, latency probes & multiplier normalization (24 platforms) | [`API_RELAY.md`](./API_RELAY.md) |
| **Multi-Agent Scoring System** | Neutrality & Risk (35%) + Data & Features (35%) + UX & Direct Connectivity (30%) | [`SCORING.md`](./SCORING.md) |
| **AI Procurement Secretary Skill** | Multi-platform inventory verification, risk filtering, executive briefs & standalone CLI toolchain | [`.agents/skills/.../SKILL.md`](./.agents/skills/card-and-relay-tracker/SKILL.md) |
| **Legal Disclaimer & Terms** | Non-commercial disclaimer, financial risk warnings & unconditional takedown procedure | [`DISCLAIMER.md`](./DISCLAIMER.md) |

---

## Curated Tier Rankings (T0 / T1)

### 1. Card & Subscription Aggregators

#### Tier 0 (Composite Score ≥ 88.0)

| Rank | Score | Platform | Official URL | Dimension Scores (Neutral / Data / UX) | Core Architecture & Features |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **1** | **93.0** | **PriceAI** | [https://priceai.cc/](https://priceai.cc/) | 80 / 100 / 100 | Open architecture, live stock curves, comprehensive price trends, clean category navigation. |
| **2** | **93.0** | **9AIB (就爱比)** | [https://9aib.com/](https://9aib.com/) | 80 / 100 / 100 | Monitors 350+ audited merchant stores, active price-drop radar, comprehensive model coverage. |

#### Tier 1 (Composite Score 78.0 ~ 87.9)

| Rank | Score | Platform | Official URL | Dimension Scores (Neutral / Data / UX) | Core Architecture & Features |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **3** | **87.2** | **OpenPrice** | [https://www.openprice.cc/](https://www.openprice.cc/) | 85 / 100 / 75 | Open-source comparison, 280+ merchant channels, real-time regional FX normalization. |
| **4** | **84.2** | **Shuita (水獭比价)** | [https://shuita.xyz/](https://shuita.xyz/) | 65 / 90 / 100 | Live aggregation across 126 merchant stores, in-stock prioritization, rapid response. |
| **5** | **82.0** | **AIFeeRadar** | [https://aifeeradar.com/](https://aifeeradar.com/) | 70 / 100 / 75 | Multi-dimensional matrix covering official subscriptions, regional tiers, and merchant quotes. |
| **6** | **81.8** | **Relay Radar** | [https://aicodex.chat/radar](https://aicodex.chat/radar) | 65 / 100 / 80 | Independent sampling, explicit in-stock floor price tags, channel counts and risk ratings. |
| **7** | **80.2** | **AIradar** | [https://airadar.vip/](https://airadar.vip/) | 70 / 90 / 80 | Weekly subscription market reports, price drop alerts, card-based interaction. |
| **8** | **80.2** | **Biwu AI (比武 AI)** | [https://biwu.ai/](https://biwu.ai/) | 70 / 90 / 80 | Tracks 280+ stores, real-time conversion across 42 official regional pricing currencies. |

---

### 2. API Relay Directory & Authenticity Benchmarks

#### Tier 0 (Composite Score ≥ 85.0)

| Rank | Score | Platform | Official URL | Dimension Scores (Neutral / Data / UX) | Core Architecture & Features |
| :---: | :---: | :--- | :--- | :---: | :--- |
| **1** | **90.0** | **RouterHubs** | [https://routerhubs.com/](https://routerhubs.com/) | 80 / 100 / 90 | Zero-commission, zero-proxy, independent availability, latency, and price snapshots across 24 relays. |
| **2** | **87.2** | **TokenAPI Scan** | [https://tokenscanai.com/](https://tokenscanai.com/) | 85 / 100 / 75 | Tracks 391 relay providers, red/black lists, targeted probes against counterfeit official routes. |
| **3** | **87.0** | **EggStriker** | [https://www.eggstriker.com/ai-api](https://www.eggstriker.com/ai-api) | 80 / 100 / 80 | Full-spectrum matrix across 144 relays, direct speed probes, model pricing & multiplier conversion. |
| **4** | **86.5** | **APITokenNav** | [https://apitokennav.com/](https://apitokennav.com/) | 70 / 100 / 90 | Indexes 105 relays, filtered by developer IDE client (Cursor/Codex) and minimum deposit thresholds. |
| **5** | **85.0** | **API Ranking** | [https://apiranking.com/](https://apiranking.com/) | 70 / 100 / 85 | Tracks domain migrations and mirror updates, multi-model price and throughput comparisons. |

---

## AI Procurement Secretary (card-and-relay-tracker)

This repository provides an integrated agentic runtime specification and a standalone Python toolchain designed for autonomous agents (Codex, Gemini, Claude Code, Cursor) and automated workflows.

---

### 1. Quick Start (Prompt to Install in 30s)

Copy and paste this prompt directly into your AI coding assistant (Codex, Claude Code, Gemini, Cursor) to install automatically:

> 📋 **One-Click Installation Prompt:**

```text
Please install and enable the AI Procurement Secretary (card-and-relay-tracker) skill from GitHub:
1. Repository URL: https://github.com/waw666waw666/awesome-ai-relay-and-cards.git
2. Copy the `.agents/skills/card-and-relay-tracker` folder and the companion `scripts/` directory into my workspace or global agent skills path (e.g. `~/.agents/skills/card-and-relay-tracker`);
3. Read its `SKILL.md`. Whenever I ask about AI subscriptions (Gemini Student Offer, ChatGPT, Claude, Cursor), in-stock finished accounts, or API relays, act as an executive procurement secretary to filter risks and deliver clean decision briefs!
```

<details>
<summary><b>🛠️ Manual Terminal Installation (Optional):</b></summary>

```bash
# Method A: Clone and copy to local or global agent skills directory
git clone https://github.com/waw666waw666/awesome-ai-relay-and-cards.git
cp -r awesome-ai-relay-and-cards/.agents/skills/card-and-relay-tracker ~/.agents/skills/

# Method B: Use directly within this workspace
cd awesome-ai-relay-and-cards
```
</details>

---

### 2. Two-Pass Verification Architecture

```
[User Request / Agent Intent]
           │
           ▼
┌────────────────────────────────────────┐
│  Phase 1: Aggregator Discovery Layer   │  ◄── targets.json (40-Site Registry)
│  - Candidate landing URL extraction    │  ◄── GATE-01: Hard Negative Blocking
│  - Eliminate out-of-stock listings     │
└──────────────────┬─────────────────────┘
                   │ Candidate Storefront URLs
                   ▼
┌────────────────────────────────────────┐
│  Phase 2: Terminal Penetration Engine  │  ◄── verify_terminal.py
│  - Anti-WAF challenge detection        │
│  - Proximity-based price/stock match   │
│  - Normalized monthly amortized rate   │
└──────────────────┬─────────────────────┘
                   │ Verified Payload (real_price, in_stock > 0, direct_url)
                   ▼
┌────────────────────────────────────────┐
│  Phase 3: High-Signal Decision Card    │  ◄── Mandatory Clickable Purchase URL
└────────────────────────────────────────┘
```

---

### 3. Seven Deterministic Decision Gates

Machine-readable policy enforced via [`references/anti_traps.md`](./.agents/skills/card-and-relay-tracker/references/anti_traps.md):

| Gate ID | Target Dimension | Severity Level | Deterministic Rule & Machine Action |
| :---: | :--- | :---: | :--- |
| **GATE-01** | **Spec Purity** | `FAIL (Hard Block)` | Immediate rejection of assisted verification/top-up services when finished accounts are requested. |
| **GATE-02** | **Price Authenticity** | `FAIL (Hard Block)` | Discard aggregator cache; terminal live checkout price takes absolute precedence. |
| **GATE-03** | **Inventory Authenticity** | `FAIL (Hard Block)` | Immediate rejection on phantom stock (`stock == 0` or pre-order queues). |
| **GATE-04** | **Delivery & Warranty** | `WARN (Downgrade)` | Flag custom-domain emails; require explicit warranty disclosure. |
| **GATE-05** | **Model Authenticity** | `FAIL (Hard Block)` | Immediate rejection if purity score < 80 or model degradation detected. |
| **GATE-06** | **Multiplier Transparency** | `REQUIRED (Normalize)` | Convert marketing promotions into effective cost per million tokens. |
| **GATE-07** | **Context Integrity** | `WARN (Flag)` | Flag silent prompt truncation beyond 8K/16K tokens and reverse-engineered endpoints. |

---

### 4. Standalone CLI Toolchain

Both scripts are built with the Python standard library with zero external dependencies:

```bash
# 1. Multi-platform AI card aggregator query with deterministic decision gates (Gemini, ChatGPT, Claude, Cursor, etc.)
python scripts/query_cards.py "gemini"
python scripts/query_cards.py "chatgpt" --limit 5

# 2. Terminal Storefront Live Price & Inventory Penetration (Anti-WAF challenge detection & anti-bait matching)
python scripts/verify_terminal.py "https://buyai.dev/" --sku "Muse" --require-tags "成品" --exclude-tags "代认证,自备" --json

# 3. Concurrency Link Health & Domain Redirect Radar (40+ Endpoints)
python scripts/check_links.py --workers 10

# Optional proxy support for cross-border network environments
python scripts/check_links.py --proxy "http://127.0.0.1:7897"
```

---

## Legal Disclaimer & Takedown Policy

1. **Informational & Non-Commercial**: This project serves as an automated benchmark snapshot and technical research aggregator. It does not constitute commercial endorsement or financial advice.
2. **Financial Caution**: Third-party subscription stores and unofficial relays carry inherent counterparty and account suspension risks. Users must adhere to on-demand, small-balance transactions.
3. **Expedited Removal**: Operators requesting delisting should file an Issue pursuant to [Section 8 of our Disclaimer](./DISCLAIMER.md#八异议沟通与侵权移除流程-notice-and-takedown). Verified requests are processed unconditionally within 7 business days.

---

## Community & Contributions

To report domain redirects, dead links, or benchmark updates, please open an [Issue](https://github.com/waw666waw666/awesome-ai-relay-and-cards/issues) or submit a Pull Request.
