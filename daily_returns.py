from load_data import  merge_columns, load_data
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

def get_daily_returns(df):
    return_df = df.copy()
    return_df = (df/df.shift(1)) -1 
    return_df.ix[0, :] = 0;
    return return_df

def plot_nifty_daily_returns():
    nifty = load_data('NIFTY')
    nifty = nifty['Close']
    daily_return = get_daily_returns(nifty)
    daily_return.hist(bins=20)
    mean = daily_return.mean()
    std = daily_return.std()
    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.show()
    print daily_return.kurtosis()

def plot_all_histograms():
    df = merge_columns("Close")
    daily_returns = get_daily_returns(df)
    daily_returns.hist(bins=20)
    #for column in df:
    #    daily_returns[column].hist(bins=20, label=column)

    plt.legend(loc='upper right')
    plt.show()

def scatter_plot():
    df = merge_columns("Close")
    df = get_daily_returns(df)
    df.plot(kind='scatter', x='NIFTY', y='BHARTIARTL')
    plt.show()
    df.plot(kind='scatter', x='NIFTY', y='RECLTD')
    beta, alpha = np.polyfit(df['NIFTY'], df['RECLTD'], 1)
    plt.plot(df['NIFTY'], beta*df['NIFTY'] + alpha, '-', color='r')
    plt.show()
    print df.corr(method='pearson')


if __name__ == '__main__':
    #plot_nifty_daily_returns()
    #plot_all_histograms()
    scatter_plot()
