---
name: a-share-trading-perspectives
description: A股交易视角整合技能。Use when the user asks to analyze A-share trading ideas through 缠论/49课, 炒股养家情绪流, 赵老哥龙头打板, 冯柳预期差, or asks for multi-perspective review of A股短线/中线决策. It routes to the right perspective, combines with real-time A-share data skills, and outputs decision checks, risk boundaries, and execution discipline rather than raw roleplay.
---

# A股交易视角整合

Use this skill as a decision-layer companion for A-share research. It does not fetch market data by itself. For current prices, hot sectors, limit-up data, fund flows, or real-time holdings, first use the appropriate data skill (`a-stock-hot`, `a-stock-analysis`, `a-stock-data`, `a-share-short-decision`, `quant-helper`) and then apply the perspective framework here.

Do not present any output as the real view of 缠中说禅、炒股养家、赵老哥、冯柳, or any other person. Say the analysis is based on public-framework abstractions when needed.

## Routing

Read only the needed reference file:

| User intent | Read |
|---|---|
| 缠论, 49课, 中枢, 背驰, 分型, 笔, 线段, 一二三类买卖点 | `references/chan-49-lessons.md` |
| 炒股养家, 情绪流, 赚钱效应, 情绪周期, 板块轮动 | `references/yangjia-emotion-cycle.md` |
| 赵老哥, 龙头战法, 打板, 连板, 二封, 封单, 次日不板即走 | `references/zhaolaoge-limit-up-leader.md` |
| 冯柳, 预期差, 弱者体系, 安全边际, 赔率, 中线逆向 | `references/fengliu-expectation-gap.md` |
| 用户要求多视角审查、交易复盘、买卖决策校准 | `references/multi-perspective-review.md` |

## Data First

For time-sensitive A-share questions, do not rely on memory.

- Current hot sectors, limit-up boards, market sentiment: use `a-stock-hot`.
- Single-stock quote, minute volume, position P/L: use `a-stock-analysis`.
- Announcements, reports, fundamentals, capital flows,龙虎榜: use `a-stock-data` or `neodata-financial-search`.
- 1-5 day candidates and logged predictions: use `a-share-short-decision`.
- Formula, screening logic, backtest, indicator implementation: use `quant-helper`.

## Output Rules

Structure the answer around decision utility:

1. State the selected perspective and why it applies.
2. Separate facts from framework judgment.
3. Give an executable checklist: entry condition, invalidation condition, position/risk boundary, review trigger.
4. Call out when the requested perspective is not suitable. For example, 冯柳视角 is not a盘中打板 framework; 赵老哥视角 is not a基本面中线 framework.
5. If data is missing, say what data is needed and avoid confident trading conclusions.

## Guardrails

- Avoid pure persona performance. Keep the perspective as an analytical lens.
- Avoid deterministic language when data is insufficient.
- Do not use the same stock for conflicting styles without explaining the time horizon conflict.
- Keep A-share T+1,涨跌停, liquidity, overnight risk, and execution delay in the risk section.
- Make clear that outputs are research support, not investment advice.

