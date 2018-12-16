from load_data import  merge_columns, load_data
import pandas as pd
import  matplotlib.pyplot as plt 

def bolliger_bands(df):
    ## Compute Bolliger bands
    rolling = df.rolling(window=20)
    mean = rolling.mean()
    std = rolling.std()
    upper_band = mean + (std*2)
    lower_band = mean - (std*2)
    return (upper_band, mean, lower_band)

if __name__ == '__main__':
    #df = merge_columns()
    #df = df/df.ix[0, :] #normalize
    nifty = load_data('NIFTY')
    nifty = nifty['Close']

    ax = nifty.plot(title="NIFTY vs Rolling Mean", label="NIFTY")
    upper, mean, lower = bolliger_bands(nifty)
    upper.plot(label="Upper bollinger band", ax=ax)
    lower.plot(label="Lower bollinger band", ax=ax)

    ax.set_xlabel('Data')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    plt.show() 
