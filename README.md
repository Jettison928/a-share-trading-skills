# A-Share Trading Skills

![A-Share](https://img.shields.io/badge/Market-A--Share-red)
![Codex Skills](https://img.shields.io/badge/Codex-Skills-blue)
![WorkBuddy](https://img.shields.io/badge/WorkBuddy-Compatible-green)
![License](https://img.shields.io/badge/Use-Research%20Only-orange)

一套面向 A 股短线交易者、市场观察者和 AI 助手用户的技能合集。

它不是普通的“问答提示词仓库”，而是把 A 股资讯、热点题材、资金流向、涨停线索、市场情绪等高频交易信息整理成可以被 Codex / WorkBuddy 调用的技能，让 AI 助手更像一个盘面信息助理，而不是只会泛泛而谈。

## 这个仓库解决什么问题

A 股信息变化快，短线交易最怕三件事：

- 只看到了新闻，却不知道它属于哪个题材。
- 只知道某个板块涨了，却不知道资金、涨停、情绪是否配合。
- 问 AI “今天 A 股有什么热点”，结果 AI 用旧知识胡说。

这个合集的目标是把这些信息流整理成结构化、可复用、适合 AI 助手调用的技能。

## 技能总览

| 技能 | 适合问什么 | 输出重点 | 数据/能力来源 |
|---|---|---|---|
| `a-stock-news` | 今日财经快讯、A 股新闻、7x24 资讯、消息面梳理 | 新闻聚合、主题分类、来源时间、原文链接 | 东方财富、同花顺、财联社等公开资讯源 |
| `a-stock-hot` | 今日热点板块、题材轮动、资金流向、涨停板、龙头股 | 热点题材、领涨个股、主力资金、市场情绪 | NeoData 金融数据能力 |

## 核心亮点

### 多源财经资讯聚合

`a-stock-news` 会聚合多路财经快讯，适合快速回答：

- 今天 A 股有什么重要新闻？
- 最近有哪些财经快讯？
- 哪些消息可能影响盘面？
- A 股、港股、美股、科技、大宗商品有没有值得关注的变化？

它的重点不是堆新闻，而是把新闻按主题归类，并保留来源、时间和链接，方便继续追溯。

### 热点题材和盘面强度观察

`a-stock-hot` 更偏交易视角，适合盘中或收盘后看：

- 今天什么板块最强？
- 主力资金流向哪里？
- 涨停板集中在哪些题材？
- 龙头股和领涨股是谁？
- 市场情绪偏强还是偏弱？

它适合做“盘面简报”，帮助你从板块、资金、涨停、情绪几个维度快速建立市场全景。

### 为 AI 助手设计的输出格式

这些技能不是只给程序员看的脚本，而是面向 AI 助手使用场景设计：

- 用自然语言触发，不需要记复杂命令。
- 输出 Markdown，便于阅读、复制和二次整理。
- 强调来源、时间、主题和结构。
- 避免让 AI 用过时训练数据回答实时行情问题。

## 推荐使用场景

| 场景 | 你可以这样问 |
|---|---|
| 盘前浏览 | 今天 A 股有什么重要消息？ |
| 盘中盯热点 | 今天 A 股热点板块有哪些？ |
| 收盘复盘 | 今天主线题材和资金流向怎么看？ |
| 涨停分析 | 今日涨停板主要集中在哪些方向？ |
| 题材跟踪 | 最近 AI、半导体、新能源有没有新消息？ |
| 情绪判断 | 今天市场赚钱效应怎么样？ |

## 仓库结构

```text
a-share-trading-skills/
├── README.md
└── skills/
    ├── a-stock-news/
    │   ├── SKILL.md
    │   ├── README.md
    │   ├── requirements.txt
    │   ├── LICENSE
    │   └── examples/
    │       └── a_stock_news.py
    └── a-stock-hot/
        └── SKILL.md
```

## 安装方式

### 安装全部技能

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Jettison928/a-share-trading-skills --path skills/a-stock-news skills/a-stock-hot
```

Windows 用户如果使用 PowerShell，可以按你的 Codex 安装目录调整脚本路径，例如：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo Jettison928/a-share-trading-skills --path skills/a-stock-news skills/a-stock-hot
```

安装后重启 Codex，新的技能才会被加载。

### 只安装新闻技能

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Jettison928/a-share-trading-skills --path skills/a-stock-news
```

### 只安装热点技能

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Jettison928/a-share-trading-skills --path skills/a-stock-hot
```

## 技能说明

### `a-stock-news`

适合做 A 股和财经消息面的快速聚合。

主要能力：

- 聚合东方财富、同花顺、财联社等公开财经资讯。
- 自动清理重复标题和无效前缀。
- 按主题分类，例如 A 股、港股、美股、科技、大宗商品、宏观等。
- 输出紧凑 Markdown，适合直接作为日报、快讯或盘前材料。

适合问题：

```text
今天 A 股有什么新闻？
最近财经快讯整理一下。
今天消息面对市场有什么影响？
7x24 财经里有什么值得关注？
```

### `a-stock-hot`

适合做 A 股热点题材和市场强度观察。

主要能力：

- 查看热门板块和题材轮动。
- 跟踪主力资金、北向资金等资金流向。
- 整理涨停板、连板股、首板股和涨停原因。
- 观察涨跌家数、成交量、赚钱效应等市场情绪指标。

适合问题：

```text
今天 A 股热点是什么？
今天哪些板块最强？
主力资金流入哪些方向？
今日涨停板集中在哪些题材？
今天市场情绪怎么样？
```

## 一个理想输出长什么样

```markdown
**A 股热点简报**

## 今日主线

| 方向 | 强度 | 代表个股 | 观察点 |
|---|---:|---|---|
| AI 算力 | 强 | 示例股份 | 资金持续流入，板块内涨停较多 |
| 半导体 | 中强 | 示例科技 | 消息催化叠加国产替代逻辑 |

## 资金流向

- 主力净流入靠前：AI 算力、半导体、机器人
- 主力净流出靠前：地产、白酒、银行

## 情绪观察

- 涨停家数增加，连板高度抬升。
- 成交量放大，短线风险偏好回升。
- 如果明日放量延续，主线可能继续扩散。
```

上面只是格式示例，不代表真实行情或投资建议。

## 适合谁使用

- 想让 AI 助手帮忙整理 A 股资讯的人。
- 做短线复盘、盘前准备、盘中热点观察的人。
- 想把财经资讯、热点题材和资金流做成固定工作流的人。
- 想构建个人交易研究助手的人。

## 不适合什么

这个仓库不做下面这些事：

- 不提供买卖点。
- 不承诺收益。
- 不替你做最终交易决策。
- 不把实时数据包装成确定性预测。

它更适合作为“信息整理层”和“研究辅助层”，帮助你更快看到市场正在发生什么。

## 后续计划

- 增加更多 A 股复盘类技能。
- 增加指数、行业、个股联动观察。
- 增加短线情绪周期记录模板。
- 增加可直接复制到日报/复盘文档的输出格式。
- 整理更多安装和使用示例。

## 风险提示

本项目仅用于信息整理、学习研究和 AI 助手能力扩展，不构成任何投资建议。A 股市场波动较大，任何交易决策都应结合个人风险承受能力、资金管理和独立判断。
