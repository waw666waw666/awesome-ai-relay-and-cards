# AI Subscription Pricing & API Relay Curated Guide (2026)

[English](./README_EN.md) | [简体中文](./README.md)

> An independent, multi-agent audited benchmark and curated directory for AI account subscriptions and developer API relays. Powered by automated terminal probes and deterministic decision gates. Zero commercial sponsorship, zero promotion bias.

---

## About the Project & Agent-Driven Engine

When procuring third-party AI subscriptions or integrating developer API relays, users and autonomous agents routinely encounter three structural hazards:

1. **Bait Pricing (Starting-Price Trap)**: Aggregators frequently display obsolete historical floor prices (e.g., $1.20 / ¥8) for sold-out trial codes, while real active in-stock packages cost significantly more.
2. **Specification Confusion & Masked Services**: Aggregators lump assisted verification services ("SheerID verification only, bring your own account") together with genuine, ready-to-use finished accounts ("Pre-activated, card-linked, credentials included") under the same SKU.
3. **Model Degradation & Hidden Token Multipliers**: Shady API relays claim official enterprise routing (e.g., Claude 3.7 / GPT-4o) while silently downgrading prompts to cheaper models or levying hidden billing multipliers on user tokens.

**This repository is both a curated directory and an integrated AI Agent Skill & Verification Engine**:
- **40-Node Embedded Registry**: [`targets.json`](./.agents/skills/card-and-relay-tracker/references/targets.json) provides structured metadata across 16 card aggregators and 24 API relays for instant in-memory resolution.
- **7-Dimension Deterministic Decision Gates**: [`anti_traps.md`](./.agents/skills/card-and-relay-tracker/references/anti_traps.md) enforces machine-readable `FAIL`, `WARN`, and `REQUIRED` constraints, with strict hard-blocking against assisted services when finished accounts are requested.
- **Two-Pass Terminal Verification Engine**: [`verify_terminal.py`](./scripts/verify_terminal.py) directly probes live storefronts, detects WAF challenges (Cloudflare, SafeLine), mitigates DOM price cross-contamination via proximity matching, and delivers direct purchase landing URLs with normalized monthly amortized pricing.

---

## Directory Navigation

| Module | Core Scope & Evaluation Focus | Document Link |
| :--- | :--- | :---: |
| **Card & Account Aggregators** | ChatGPT, Claude, Gemini subscriptions, finished accounts & redemption codes (16 platforms) | [`CARDS.md`](./CARDS.md) |
| **API Relay Benchmarks** | Developer API endpoints, authenticity audits, latency probes & multiplier normalization (24 platforms) | [`API_RELAY.md`](./API_RELAY.md) |
| **Multi-Agent Scoring System** | Neutrality & Risk (35%) + Data & Features (35%) + UX & Direct Connectivity (30%) | [`SCORING.md`](./SCORING.md) |
| **Agent Skill & Toolchain** | Two-pass penetration verification SOP, 7-gate decision matrix & Python automation tools | [`.agents/skills/.../SKILL.md`](./.agents/skills/card-and-relay-tracker/SKILL.md) |
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

## AI Agent Skill & Terminal Verification Engine

This repository provides an integrated agentic runtime specification and a standalone Python toolchain designed for autonomous agents (Codex, Gemini, Claude Code, Cursor) and automated workflows.

### 1. Two-Pass Verification Architecture

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

### 2. Interaction Contract Matrix (Agent Invocation)

| Intent Pattern | Prompt Contract | Engine Execution Pipeline |
| :--- | :--- | :--- |
| **Procure Finished Account** | *"Find genuine, in-stock ChatGPT Plus 4-month student finished accounts. Ready to use only, exclude assisted verification."* | 1. Load `spec_filters.finished_account.negative_keywords` to hard-block assisted services.<br>2. Query Tier 0/1 aggregators for candidates.<br>3. Execute `verify_terminal.py` with `--require-tags "成品"` and `--exclude-tags "代认证,自备"`.<br>4. Output verified decision card with clickable purchase URLs. |
| **Storefront Price Audit** | *"Verify current price and stock status for Muse at https://buyai.dev/."* | 1. Execute `verify_terminal.py "https://buyai.dev/" --sku "Muse" --json`.<br>2. Extract live checkout price, active stock count, and warranty terms.<br>3. Flag any WAF challenges or price mismatches. |
| **Relay Authenticity Audit** | *"Recommend verified, non-degraded Claude 3.7 Sonnet API relays."* | 1. Query `targets.json` Tier 0 relay benchmarks (RouterHubs, TokenAPI Scan).<br>2. Enforce GATE-05 (Authenticity probe score ≥ 80).<br>3. Calculate real per-1M-token cost using GATE-06 formula (`Official_Price × Group_Ratio × Model_Ratio`). |
| **Full Link Health Sweep** | *"Run automated health check and domain migration radar on all links."* | 1. Execute `check_links.py --workers 10`.<br>2. Track 301/302 domain redirects (`REDIRECT_CHANGED`) and server errors. |

### 3. Seven Deterministic Decision Gates (Machine-Readable)

Full specification available in [`references/anti_traps.md`](./.agents/skills/card-and-relay-tracker/references/anti_traps.md):

- **GATE-01 (Spec Purity)**: Immediate `FAIL` on services requiring buyer's own account when finished account is requested.
- **GATE-02 (Price Authenticity)**: Immediate `FAIL` on aggregator cache divergence; terminal checkout price takes absolute precedence.
- **GATE-03 (Inventory Authenticity)**: Immediate `FAIL` on phantom stock (`stock == 0` or pre-order queues).
- **GATE-04 (Account Security & Warranty)**: `WARN` on disposable custom-domain email addresses; require explicit warranty disclosure.
- **GATE-05 (Model Authenticity)**: Immediate `FAIL` if purity score < 80 or model degradation detected.
- **GATE-06 (Multiplier Transparency)**: `REQUIRED` conversion to effective cost per million tokens.
- **GATE-07 (Context Integrity)**: `WARN` on silent prompt truncation beyond 8K/16K tokens.

---

## Standalone CLI Toolchain

Both scripts are built with the Python standard library with zero external dependencies:

```bash
# 1. Terminal Storefront Live Price & Inventory Penetration
python scripts/verify_terminal.py "https://buyai.dev/" --sku "Muse" --require-tags "成品" --exclude-tags "代认证,自备" --json

# 2. Concurrency Link Health & Domain Redirect Radar (40+ Endpoints)
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
