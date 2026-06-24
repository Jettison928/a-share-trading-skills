# 多视角交易审查

Use when the user asks for a combined review of a trade idea, holding, watchlist, or daily plan.

## Default Review Order

1. Facts: summarize price, volume, sector,资金, news, and current market sentiment from data skills.
2. Time horizon: classify the idea as intraday, 1-5 day short-term, swing, or 3-6 month expectation-gap trade.
3. Apply only matching perspectives:
   - Intraday board/leader: 赵老哥 + 炒股养家.
   - 1-5 day momentum: 炒股养家 + 缠论 + short-term signal engine.
   - Technical structure: 缠论.
   - Medium-term valuation mismatch: 冯柳.
4. Identify conflicts. Example: 冯柳 says wait for pessimistic pricing, while 赵老哥 requires immediate strength confirmation.
5. Produce an action table.

## Output Template

```markdown
**交易审查**

**事实基础**
- 市场情绪:
- 板块/题材:
- 个股状态:

**适用视角**
- 主视角:
- 辅助视角:
- 不适用视角:

**执行条件**
| 项目 | 条件 |
|---|---|
| 介入 | ... |
| 加仓 | ... |
| 止损/失效 | ... |
| 止盈/复盘 | ... |
| 仓位 | ... |

**主要风险**
- ...
```

## Conflict Handling

- 龙头打板 and 冯柳逆向 often conflict. Do not merge them into one entry rule.
- 缠论 small-level buy points can conflict with market emotion. If emotion is retreating, reduce conviction.
- 情绪流 can support offense, but individual stock execution still needs clear invalidation.

