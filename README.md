# A-Share Trading Skills

![A-Share](https://img.shields.io/badge/Market-A--Share-red)
![Trading](https://img.shields.io/badge/Focus-Trading%20Workflow-orange)
![Codex Skills](https://img.shields.io/badge/Codex-Skills-blue)
![WorkBuddy](https://img.shields.io/badge/WorkBuddy-Compatible-green)
![Research Only](https://img.shields.io/badge/Use-Research%20Only-lightgrey)

一个面向 A 股交易研究、短线复盘、热点跟踪、资金观察和量化辅助的 AI 技能合集。

它不是简单堆几个脚本，而是把 A 股交易中常用的信息流拆成一套可复用的技能：新闻、热点、行情、数据、技术指标、资金流、短线决策、量化公式、金融搜索。你可以把它理解成一个给 Codex / WorkBuddy 使用的“个人 A 股研究工作台”。

## 为什么做这个合集

A 股交易信息密度很高，真正耗时间的往往不是看一条新闻，而是把这些信息串起来：

- 今天有什么重要消息？
- 哪些题材正在发酵？
- 板块强度和资金是否共振？
- 个股实时量能有没有异常？
- 技术指标是否支持继续观察？
- 今天的盘面情绪适合进攻还是防守？
- 能不能把选股条件固化成公式或回测逻辑？

这个仓库的目标就是让 AI 助手不再只会泛泛解释概念，而是能围绕 A 股交易工作流进行信息获取、整理、分析和输出。

## 能力地图

| 层级 | 解决的问题 | 对应技能 |
|---|---|---|
| 市场资讯层 | 今天有什么财经新闻、A 股消息、宏观事件 | `a-stock-news` |
| 热点题材层 | 什么板块最强、资金流向哪里、涨停集中在哪 | `a-stock-hot` |
| 实时行情层 | 个股价格、涨跌幅、分时量能、主力动向 | `a-stock-analysis` |
| 全栈数据层 | 行情、研报、公告、财报、龙虎榜、融资融券 | `a-stock-data` |
| 技术指标层 | K 线、均线、MACD、KDJ、RSI、BOLL、CCI | `ashareskill` |
| 金融搜索层 | 股票、基金、指数、宏观、外汇、大宗商品查询 | `neodata-financial-search` |
| 短线决策层 | 1-5 日短线信号、强势股扫描、预测记录 | `a-share-short-decision` |
| 交易视角层 | 缠论、情绪流、龙头战法、预期差的决策审查 | `a-share-trading-perspectives` |
| 量化辅助层 | 通达信/同花顺公式、选股逻辑、简单回测 | `quant-helper` |

## 技能清单

### `a-stock-news` - A 股财经新闻聚合

适合快速整理财经快讯和消息面。

主要能力：

- 聚合东方财富、同花顺、财联社等公开财经资讯。
- 自动去重、清洗标题、保留来源和链接。
- 按主题整理 A 股、港股、美股、科技、宏观、大宗商品等信息。
- 输出适合日报、盘前浏览、复盘引用的 Markdown。

适合这样问：

```text
今天 A 股有什么新闻？
最近财经快讯整理一下。
今天消息面对市场有什么影响？
```

### `a-stock-hot` - A 股热点题材与资金流

适合观察当天市场主线、热点板块、涨停板和赚钱效应。

主要能力：

- 热点板块和题材轮动。
- 主力资金、北向资金等资金流向。
- 涨停板、连板股、首板股、涨停原因。
- 市场情绪、涨跌家数、成交量和赚钱效应。

适合这样问：

```text
今天 A 股热点是什么？
今天哪些板块最强？
主力资金流入哪些方向？
今日涨停板集中在哪些题材？
```

### `a-stock-analysis` - 实时行情与分时量能分析

适合盯单只股票或持仓股票的实时状态。

主要能力：

- 查询沪深个股实时价格、涨跌幅、成交量。
- 分析分时量能分布，例如早盘放量、尾盘放量。
- 识别主力抢筹、出货等量价信号。
- 支持持仓管理和盈亏分析。

适合这样问：

```text
帮我看一下 600519 今天实时走势。
这只股票有没有放量？
我的持仓现在盈亏怎么样？
```

### `a-stock-data` - A 股全栈数据工具包

适合做更深入的个股、行业、资金和基本面研究。

主要能力：

- 行情数据：通达信、腾讯、百度 K 线等。
- 研报数据：东方财富、同花顺、iWenCai 等。
- 资金数据：融资融券、大宗交易、资金流、北向等。
- 新闻公告：个股新闻、巨潮公告。
- 基础数据：财报、F10、三大表。
- 适合个股估值、题材归因、行业轮动、解禁预警、产业链调研。

适合这样问：

```text
查一下某只股票最近的公告和研报。
帮我看一下这个行业最近资金流。
这个公司基本面数据怎么样？
```

### `ashareskill` - K 线与技术指标数据

适合获取历史 K 线和完整技术指标，用于技术分析或策略研究。

主要能力：

- 支持单只股票或股票池批量查询。
- 支持日线、周线、月线。
- 输出 MA、MACD、KDJ、RSI、BOLL、CCI 等指标。
- 可用于策略回测、量化分析、指标验证。

适合这样问：

```text
获取贵州茅台最近一年的日线和技术指标。
批量导出这些股票的 MACD 和 RSI。
```

### `neodata-financial-search` - 自然语言金融数据搜索

适合跨市场、跨资产查询金融数据。

主要能力：

- 查询 A 股、港股、美股、基金、指数。
- 查询宏观经济、外汇、大宗商品。
- 支持财务报表、资金流、评级、公告等金融数据。
- 作为其他技能的数据底座之一。

适合这样问：

```text
查询贵州茅台当前股价。
最近黄金价格怎么走？
某个基金今年收益怎么样？
```

### `a-share-short-decision` - A 股短线交易决策辅助

适合 1-5 日短线研究、强势股扫描和信号记录。

主要能力：

- 市场情绪、板块轮动、强势股扫描。
- 资金流确认和短线信号评分。
- 预测记录、次日对比、策略配置优化。
- 包含每日推荐和配置优化两个子技能。

适合这样问：

```text
今天短线有哪些强势方向？
帮我跑一下明天的短线候选。
对昨天的短线预测做个复盘。
```

### `a-share-trading-perspectives` - A 股交易视角整合

适合把实时数据和交易想法放进不同交易框架里做决策审查。

主要能力：

- 按需调用 49 课缠论、炒股养家情绪流、赵老哥龙头打板、冯柳预期差视角。
- 区分短线打板、1-5 日动量、技术结构和 3-6 个月预期差交易。
- 输出介入条件、失效条件、仓位边界和复盘触发点。
- 与实时行情、热点、资金、短线信号、量化公式技能配合使用。

适合这样问：

```text
用缠论和情绪周期一起审一下这只票。
这个打板机会按赵老哥视角能不能做？
用冯柳预期差框架看一下这笔中线逻辑。
```

### `quant-helper` - 量化公式与回测辅助

适合把交易想法转成公式、指标或简单回测逻辑。

主要能力：

- 编写通达信、同花顺选股公式。
- 编写技术指标公式。
- 计算技术指标数据。
- 对简单交易策略做回测验证。
- 生成量化精选股票池。

适合这样问：

```text
帮我写一个放量突破 20 日线的通达信选股公式。
把这个交易思路改成同花顺公式。
回测一下这个简单条件的胜率。
```

## 推荐工作流

### 盘前

1. 用 `a-stock-news` 看隔夜和盘前消息。
2. 用 `a-stock-data` 查重点个股公告、研报、基本面变化。
3. 用 `a-share-short-decision` 生成短线候选观察池。

### 盘中

1. 用 `a-stock-hot` 看热点板块和资金方向。
2. 用 `a-stock-analysis` 盯重点个股分时量能。
3. 用 `neodata-financial-search` 快速补查指数、板块、基金或商品数据。

### 收盘后

1. 用 `a-stock-hot` 整理主线、涨停和情绪。
2. 用 `ashareskill` 拉 K 线和技术指标。
3. 用 `a-share-trading-perspectives` 做交易视角审查。
4. 用 `quant-helper` 把观察到的规律固化成公式或策略。
5. 用 `a-share-short-decision` 做次日候选和预测记录。

## 安装方式

### 一次安装全部技能

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Jettison928/a-share-trading-skills --path skills/a-stock-news skills/a-stock-hot skills/a-stock-analysis skills/a-stock-data skills/ashareskill skills/neodata-financial-search skills/a-share-short-decision skills/a-share-trading-perspectives skills/quant-helper
```

Windows PowerShell 示例：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-installer\scripts\install-skill-from-github.py" --repo Jettison928/a-share-trading-skills --path skills/a-stock-news skills/a-stock-hot skills/a-stock-analysis skills/a-stock-data skills/ashareskill skills/neodata-financial-search skills/a-share-short-decision skills/a-share-trading-perspectives skills/quant-helper
```

安装完成后，重启 Codex 才会加载新技能。

### 单独安装某一个技能

把最后的路径换成你想安装的技能即可：

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Jettison928/a-share-trading-skills --path skills/a-stock-hot
```

可用路径：

```text
skills/a-stock-news
skills/a-stock-hot
skills/a-stock-analysis
skills/a-stock-data
skills/ashareskill
skills/neodata-financial-search
skills/a-share-short-decision
skills/a-share-trading-perspectives
skills/quant-helper
```

## 仓库结构

```text
a-share-trading-skills/
├── README.md
└── skills/
    ├── a-stock-news/
    ├── a-stock-hot/
    ├── a-stock-analysis/
    ├── a-stock-data/
    ├── ashareskill/
    ├── neodata-financial-search/
    ├── a-share-short-decision/
    ├── a-share-trading-perspectives/
    └── quant-helper/
```

## 示例输出风格

```markdown
**A 股盘面简报**

## 今日主线

| 方向 | 强度 | 代表个股 | 观察点 |
|---|---:|---|---|
| AI 算力 | 强 | 示例股份 | 板块放量，资金持续流入 |
| 半导体 | 中强 | 示例科技 | 消息催化，国产替代逻辑发酵 |

## 资金与情绪

- 主力净流入靠前：AI 算力、半导体、机器人
- 涨停集中方向：算力、先进封装、低空经济
- 市场情绪：成交放大，短线风险偏好回升

## 明日观察

- 主线是否继续放量。
- 龙头是否继续封板。
- 后排补涨是否扩散。
```

以上只是格式示例，不代表真实行情或投资建议。

## 适合谁

- 想让 AI 助手辅助整理 A 股资讯的人。
- 做短线复盘、盘前准备、盘中热点观察的人。
- 想把选股条件、技术指标和交易规则固化成工具的人。
- 想搭建个人 A 股研究工作流的人。

## 不适合什么

这个合集不提供确定性买卖建议，不承诺收益，也不会替你承担交易风险。它更适合作为信息整理、研究分析和交易流程辅助工具。

## 公开仓说明

为了适合公开发布，本仓库只保留技能源码、说明文件、脚本和必要资源。已排除本机运行日志、缓存、用户元数据、Python 编译缓存和临时凭证文件。

## 风险提示

本项目仅用于信息整理、学习研究和 AI 助手能力扩展，不构成任何投资建议。A 股市场波动较大，任何交易决策都应结合个人风险承受能力、资金管理和独立判断。
