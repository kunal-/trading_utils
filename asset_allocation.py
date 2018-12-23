import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from load_data import  merge_columns
from daily_returns import get_daily_returns
from scipy.optimize import minimize

def get_sharpe_ratio(weights, args):
    return -1 * np.sum(args[0]*weights)/ np.sum(args[1]*weights)

if __name__ == '__main__':
    df = merge_columns("Close")
    close = df.ix[600:, :]
    df = df.ix[:600, :]
    df = get_daily_returns(df)
    df = df.ix[:, 1:]
    close = close.ix[:, 1:]
    mean = df.mean(axis=0)
    std = df.std(axis=0)
    args = np.asarray([mean, std])
    weights = np.random.random(mean.shape)
    weights = weights/weights.sum()
    bounds = [(0, .1) for _ in df.columns]
    minima = minimize(get_sharpe_ratio, weights, args=args, method='SLSQP',constraints=[{'type':'eq', 'fun': lambda x: x.sum() - 1 }], bounds=bounds, options={'disp':True})
    total_return = 0 
    for weight, stock in zip(minima.x, df.columns):
        if weight:
            print stock, " : ", weight
            total_return += (close[stock]/close.ix[0, stock] -1)*weight
    total_return.plot()
    print "Returns: ", total_return[-1]
    plt.show()

