import akshare as ak
import pandas as pd

stocks = [('300383', '首都在线'), ('000815', '美利云')]
for code, name in stocks:
    try:
        df = ak.stock_individual_fund_flow(stock=code, market='sz' if code.startswith('0') or code.startswith('3') else 'sh')
        print(f'\n===== {name}({code}) 资金流向 (最近5日) =====')
        cols = [c for c in ['日期','主力净流入-净额','主力净流入-净占比','超大单净流入-净额','大单净流入-净额'] if c in df.columns]
        print(df[cols].tail(5).to_string(index=False))
    except Exception as e:
        print(f'{name} 资金流向获取失败: {e}')
