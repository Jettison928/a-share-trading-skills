# A-Stock-News 🚀

> 免费聚合东方财富、同花顺、财联社三家A股财经快讯，输出AI HOT风格紧凑格式。

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## ✨ 特性

- 🆓 **完全免费**：无需API Key，直接调用三家媒体的内部JSON接口
- 🔄 **三路聚合**：东方财富 + 同花顺 + 财联社，覆盖面广
- 🧹 **智能去重**：基于中文标题标准化 + 前缀去除 + 前20字匹配
- 📊 **主题分类**：自动分类为美股/科技、A股/港股、大宗商品、宏观/利率、地缘政治、综合快讯
- 📝 **AI HOT风格输出**：紧凑排版，一目了然
- 🤖 **AI助手技能**：可直接作为WorkBuddy/CherryStudio技能安装

---

## 🚀 快速开始

### 安装依赖

```bash
pip install requests
```

### 运行脚本

```bash
python examples/a_stock_news.py
```

输出文件：`a_stock_news_output.md`

---

## 📖 使用示例

```python
from a_stock_news import fetch_all, dedup, format_output

# 获取三路新闻
items = fetch_all()

# 去重
unique_items = dedup(items)

# 格式化输出
output = format_output(unique_items)
print(output)
```

---

## 🏗️ 项目结构

```
a-stock-news/
├── README.md              # 本文件
├── SKILL.md               # AI助手技能文件（WorkBuddy/CherryStudio）
├── examples/
│   └── a_stock_news.py  # 完整可运行脚本
├── docs/
│   ├── tencent-cloud-article.md  # 腾讯云+社区发布文章
│   └── video-script.md          # 短视频脚本
├── requirements.txt
└── LICENSE
```

---

## 🔧 核心功能

### 1. 数据源

| 来源 | 接口类型 | 更新频率 | 免费 |
|------|---------|---------|------|
| 东方财富 | JSONP | 实时 | ✅ |
| 同花顺 | JSON | 实时 | ✅ |
| 财联社 | JSON (需sign) | 实时 | ✅ |

### 2. 中文去重算法

采用启发式规则（而非通用NLP算法）：

```python
def dedup_key(title):
    # 1. 去除前缀（财联社X月X日电：）
    t = strip_prefix(title)
    # 2. 标准化（去标点）
    t = normalize(t)
    # 3. 取前20字作为去重键
    return t[:20]
```

**准确率**：约85%，对于快讯聚合场景已够用。

### 3. 主题分类

基于关键词匹配：

```python
RULES = {
    '🇺🇸 美股/科技': ['美股', '纳斯达克', 'SpaceX', '苹果', 'AI'],
    '📈 A股/港股': ['A股', '沪指', '恒生', '涨停'],
    '🛢️ 大宗商品': ['原油', '黄金', '铜', 'LME'],
    '💹 宏观/利率': ['美联储', '降息', '国债', '央行'],
    '🌍 地缘政治': ['伊朗', '特朗普', '关税'],
}
```

---

## 🤖 作为AI助手技能使用

如果你使用 **WorkBuddy** 或 **CherryStudio**，可以直接安装本技能：

### 方法一：从源码安装

将 `SKILL.md` 放到 `~/.workbuddy/skills/a-stock-news/` 目录下。

### 方法二：通过技能市场安装（待上架）

```
安装技能 a-stock-news
```

安装后，只需对AI助手说：

```
A股新闻
```

助手会自动运行聚合脚本，返回格式化后的财经快讯。

---

## ⚠️ 注意事项

1. **合规使用**：本项目的接口均为各平台公开可访问的接口，仅用于学习研究，请遵守各平台的服务条款。
2. **请求频率**：建议不要过高频率请求，避免给源站造成压力。
3. **投资建议**：新闻数据仅供参考，不构成投资建议。

---

## 🔗 相关资源

- [china-finance-rss](https://github.com/书上的蚂蚁/china-finance-rss) - 中文财经RSS聚合（本项目数据源的参考来源）
- [AI HOT Skill](https://github.com/...) - 灵感来源，AI领域资讯聚合

---

## 🤝 贡献

欢迎提交PR！特别是：
- 新的数据源
- 更优的去重算法
- Bug修复

---

## 📄 开源协议

[MIT License](LICENSE)

---

## ⭐ Star History

如果这个项目对你有帮助，请点一个Star ⭐

---

**作者**：AI辅助开发实践者  
**写于**：2026年6月23日
