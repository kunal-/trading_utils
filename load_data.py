import pandas as pd
from datetime import date
import stocks_time

symbol = 'NIFTY'

def load_data(symbol):
    return pd.read_csv('data/{}.csv'.format(symbol), index_col='Date', parse_dates=True)

def merge_columns(label='Close'):
    dates = pd.date_range(start=date(*stocks_time.start_date), end=date(*stocks_time.end_date))
    df = pd.DataFrame(index=dates)
    for symbol in stocks_time.symbols:
        dfs = load_data(symbol);
        dfs = dfs.ix[:, [label]]
        dfs = dfs.rename(columns={label:symbol})
        df = df.join(dfs, how='inner')
    return df

