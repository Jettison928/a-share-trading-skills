import akshare as ak
import pandas as pd

stocks = [('300383', '首都在线'), ('000815', '美利云')]
for code, name in stocks:
    try:
        df = ak.stock_zh_a_hist(symbol=code, period='daily', start_date='20260310', end_date='20260316', adjust='qfq')
        print(f'\n===== {name}({code}) =====')
        print(df[['日期','开盘','收盘','最高','最低','成交量','涨跌幅']].tail(5).to_string(index=False))
        # 计算5日均线
        if len(df) >= 5:
            ma5 = df['收盘'].rolling(5).mean().iloc[-1]
            print(f'MA5: {ma5:.2f}')
        # 今日数据
        today = df[df['日期'] == '2026-03-16']
        if not today.empty:
            row = today.iloc[0]
            print(f"今日涨跌幅: {row['涨跌幅']:.2f}%  收盘: {row['收盘']:.2f}")
    except Exception as e:
        print(f'{name} 获取失败: {e}')
