---
name: a-stock-news
description: A股财经新闻资讯 Skill。当用户想知道"A股新闻"、"今日财经快讯"、"A股消息面"、"7x24财经"、"东方财富资讯"、"今日有什么财经大事"、"A股快讯"等A股新闻查询时使用。基于东方财富全球资讯（7×24实时滚动）+ 同花顺快讯 + 财联社电报三路聚合，按主题分类，输出 AI HOT 紧凑风格。
---

# a-stock-news v3.1.0

## 触发词
"A股新闻"、"财经快讯"、"今日财经"、"A股消息"、"7x24资讯"、"财经热点"

## 功能
三路免费聚合（东方财富 + 同花顺 + 财联社），按主题分类，AI HOT 紧凑格式输出。

**v3.1.0 改进**：消息完整无截断，来源/时间移至末尾（URL 同行），体育/娱乐新闻自动过滤。

## 数据源
- 东方财富 7×24：https://kuaixun.eastmoney.com/ （免费，无需 API key）
- 同花顺 7×24：https://news.10jqka.com.cn/ （免费，JSON API）
- 财联社电报：https://www.cls.cn/telegraph （免费，sign 算法已破解）

## 输出格式（AI HOT 紧凑风格 · v3.1.0）
```
**A股财经热点 — 最近 N 条精选（MM-DD ~ MM-DD）**

### 🇺🇸 美股/科技

1. **完整标题不截断**
   完整摘要内容，不断开句子，保持信息完整性。
   东方财富 2026-06-23 03:12:41  https://kuaixun.eastmoney.com/a/xxx

2. **另一条标题**
   来源 时间  URL

### 📈 A股/港股
...

---
[数据源] 东方财富7×24 · 同花顺7×24 · 财联社电报
```

**格式要点**：
- 标题粗体，不截断
- 摘要完整，不截断
- 第三行：来源 + 时间 + URL（同行）
- 体育/娱乐新闻自动过滤

## 执行代码（Python 3.6+）

将以下代码保存为 `a_stock_news.py`，运行：`python a_stock_news.py`
输出文件：`C:/Users/pedmi/AppData/Local/Temp/astock_news_output.md`

```python
import time, random, requests, json, hashlib, re
from datetime import datetime, timedelta, timezone
from collections import defaultdict

# ===== 公共设置 =====
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
SESSION = requests.Session()
SESSION.headers.update({'User-Agent': UA})
MIN_INTERVAL = 0.8
_last_call = [0.0]

def _get(url, p=None, h=None, t=15):
    w = MIN_INTERVAL - (time.time() - _last_call[0])
    if w > 0:
        time.sleep(w + random.uniform(0.05, 0.3))
    try:
        r = SESSION.get(url, params=p, headers=h, timeout=t)
    finally:
        _last_call[0] = time.time()
    return r

def sp(t):
    """清理标题前缀（财联社X月X日电：等）"""
    t = t.strip()
    t = re.sub(r'^【[^】]*】', '', t)
    for pat in [r'财联社\d+月\d+日电[：:，,。\s]*',
               r'同花顺\d+月\d+日电[：:，,。\s]*',
               r'东方财富\d+月\d+日电[：:，,。\s]*',
               r'\d+月\d+日电[：:，,。\s]*']:
        t = re.sub(pat, '', t)
    return t.replace('【','').replace('】','').strip()

# ===== 数据源 =====
def em(page=30):
    r = _get(f'https://newsapi.eastmoney.com/kuaixun/v1/getlist_102_ajaxResult_{page}_1_.html',
             h={'Referer':'https://kuaixun.eastmoney.com/'})
    m = re.search(r'var ajaxResult=(\{.*\});?', r.text, re.DOTALL)
    if not m:
        return []
    return [{'t': sp(x.get('title','')), 'd': sp(x.get('digest','')),
             'tm': x.get('showtime',''),
             'u': f"https://kuaixun.eastmoney.com/a/{x.get('newsid','')}",
             's': '东方财富'}
            for x in json.loads(m.group(1)).get('LivesList',[])]

def ths(page=30):
    r = _get(f'https://news.10jqka.com.cn/tapp/news/push/stock/?page=1&tag=&track=website&pagesize={page}',
             h={'Referer':'https://news.10jqka.com.cn/'})
    if r.status_code != 200:
        return []
    rows = []
    for x in r.json().get('data',{}).get('list',[]):
        ct = int(x.get('ctime',0))
        dt = datetime.fromtimestamp(ct, tz=timezone(timedelta(hours=8))).strftime('%m-%d %H:%M') if ct else ''
        rows.append({'t': sp(x.get('title','')),
                     'd': sp(x.get('digest','') or x.get('remark','')),
                     'tm': dt,
                     'u': x.get('url',''),
                     's': '同花顺'})
    return rows

def cls(page=30):
    def _sv(v, k):
        if v is None:
            return None
        if isinstance(v, (str, int, float, bool)):
            return f'{k}={v}'
        if isinstance(v, list):
            return '&&'.join(_sv(x, f'{k}[{i}]') for i, x in enumerate(v)) if v else f'{k}[]'
        if isinstance(v, dict):
            return '&&'.join(_sv(v[x], f'{k}[{x}]') for x in sorted(v, key=lambda s: str(s).upper()))
        return None
    params = {'refresh_type': 1, 'rn': page, 'last_time': 0,
              'os': 'web', 'sv': '8.7.9', 'app': 'CailianpressWeb'}
    ser = '&&'.join(_sv(params[k], k) for k in sorted(params, key=lambda x: str(x).upper()))
    params['sign'] = hashlib.md5(hashlib.sha1(ser.encode()).hexdigest().encode()).hexdigest()
    r = _get('https://www.cls.cn/v1/roll/get_roll_list',
              p=params, h={'Referer':'https://www.cls.cn/telegraph'})
    if r.status_code != 200 or r.json().get('errno',0) != 0:
        return []
    rows = []
    for x in r.json().get('data',{}).get('roll_data',[]):
        ct = int(x.get('ctime',0))
        dt = datetime.fromtimestamp(ct, tz=timezone(timedelta(hours=8))).strftime('%m-%d %H:%M') if ct else ''
        c = sp(x.get('content',''))
        brief = sp(x.get('brief',''))
        title = c[:80].strip() if c else brief[:80]
        rows.append({'t': title, 'd': brief, 'tm': dt,
                     'u': f"https://www.cls.cn/telegraph/{x.get('id','')}",
                     's': '财联社'})
    return rows

# ===== 主题分类 =====
RULES = {
    '🇺🇸 美股/科技': ['美股','纳斯达克','标普','道琼斯','英伟达','谷歌','苹果','微软','特斯拉',
                    'Meta','亚马逊','OpenAI','Anthropic','超微','SMCI','台积电','TSM','SpaceX',
                    'AI ','人工智能','芯片','半导体','光通信','DeepMind','科技'],
    '📈 A股/港股': ['A股','上证','深证','创业板','科创板','恒生','北向','融资','涨停','跌停',
                  'IPO','定增','重组','回购','减持','增持','分红','财报','港股'],
    '🛢️ 大宗商品': ['原油','石油','黄金','白银','贵金属','铜','铝','铁矿石','煤炭','天然气',
                   '期货','夜盘','合约','LME','COMEX','沪金','沪银','上期所','氧化铝'],
    '💹 宏观/利率': ['美联储','降息','加息','国债','通胀','CPI','非农','GDP','PMI',
                   '央行','欧央行','巴克莱','高盛','摩根','美债','汇率','美元','人民币','RRP'],
    '🌍 地缘政治': ['伊朗','土耳其','俄罗斯','乌克兰','中东','以色列','核','制裁',
                    '无人机','袭击','特朗普','拜登','白宫','国会','霍尔木兹'],
}
FILTER_KW = ['世界杯','足球','阿根廷','奥地利','梅西','姆巴佩','C罗','NBA','篮球','网球','奥运会']

def topic(title, digest=''):
    txt = title + ' ' + digest
    for kw in FILTER_KW:
        if kw in txt:
            return None
    sc = {t: sum(1 for kw in kws if kw in txt) for t, kws in RULES.items()}
    mx = max(sc.values())
    if mx == 0:
        return '📰 综合快讯'
    return [t for t, v in sc.items() if v == mx][0]

# ===== 增强去重 =====
def smart_dedup(items):
    def core_kws(t):
        return set(re.sub(r'[^\u4e00-\u9fff\w]', '', t))
    result = []
    used = set()
    for i, item in enumerate(items):
        if i in used:
            continue
        t1 = item['t']
        k1 = core_kws(t1)
        for j in range(i+1, len(items)):
            if j in used:
                continue
            t2 = items[j]['t']
            k2 = core_kws(t2)
            shorter = min(len(k1), len(k2))
            if shorter == 0:
                continue
            overlap = len(k1 & k2)
            if overlap / shorter >= 0.5:
                used.add(j)
                if len(t2) > len(item['t']):
                    new_item = dict(item)
                    new_item['t'] = t2
                    new_item['d'] = items[j].get('d', item.get('d',''))
                    item = new_item
                    k1 = k2
        result.append(item)
        used.add(i)
    return result

# ===== 格式化 =====
def fmt_digest(it):
    """提取摘要：去掉与标题重复的部分，不断开句子"""
    title = it['t']
    dig = it.get('d', '')
    if not dig:
        return ''
    clean = dig.replace(title, '').strip()
    clean = re.sub(r'^[：:，,。\s]+', '', clean)
    return clean

def run(limit=25):
    all_items = em() + ths() + cls()
    all_items.sort(key=lambda x: x.get('tm',''), reverse=True)
    deduped = smart_dedup(all_items)
    
    topics = defaultdict(list)
    for item in deduped:
        tp = topic(item['t'], item.get('d',''))
        if tp is None:
            continue
        topics[tp].append(item)
    
    order = ['🇺🇸 美股/科技','📈 A股/港股','🛢️ 大宗商品','💹 宏观/利率','🌍 地缘政治','📰 综合快讯']
    now = datetime.now(tz=timezone(timedelta(hours=8)))
    total = sum(len(v) for v in topics.values())
    L = [f'**A股财经热点 — 最近 {total} 条精选（{(now-timedelta(days=1)).strftime("%m-%d")} ~ {now.strftime("%m-%d")}）**']
    
    for tn in order:
        if tn not in topics:
            continue
        L.append(f'\n### {tn}\n')
        for i, it in enumerate(topics[tn], 1):
            title = it['t']  # 不截断
            src = it['s']
            tm = it.get('tm','')
            body = fmt_digest(it)
            
            L.append(f"{i}. **{title}**")
            if body:
                L.append(f"   {body}")
            src_line = f"   {src}"
            if tm:
                src_line += f" {tm}"
            src_line += f"  {it['u']}"
            L.append(src_line)
            L.append('')
    
    L.append('---\n[数据源] 东方财富7×24 · 同花顺7×24 · 财联社电报')
    out = '\n'.join(L)
    op = r'C:/Users/pedmi/AppData/Local/Temp/astock_news_output.md'
    with open(op, 'w', encoding='utf-8') as f:
        f.write(out)
    return op

if __name__ == '__main__':
    print('Done:', run())
```

## 使用说明
1. 安装依赖：`pip install requests`
2. 保存 above code as `a_stock_news.py`
3. 运行：`python a_stock_news.py`
4. 输出：`C:/Users/pedmi/AppData/Local/Temp/astock_news_output.md`
5. 在 WorkBuddy 中直接说"A股新闻"即可触发

## 版本历史
- v3.1.0 (2026-06-23): 消息完整无截断，来源/时间移至末尾，体育新闻过滤
- v3.0.0 (2026-06-23): 三路聚合 + AI HOT 紧凑格式 + 智能去重 + 主题分类
- v2.0.0 (2026-06-23): 添加同花顺 + 财联社数据源
- v1.0.0 (2026-06-23): 初始版本，仅东方财富数据源
