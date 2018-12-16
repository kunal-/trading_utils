from nsepy import get_history
from datetime import date	
import stocks_time 


def download_data(symbol):
	index = False
	if (symbol is "NIFTY"): index = True 
	data = get_history(symbol=symbol, index=index,
		start=date(*stocks_time.start_date), end=date(*stocks_time.end_date))
	data.to_csv('data/{}.csv'.format(symbol))

if __name__ == '__main__':
	for symbol in stocks_time.symbols:
		download_data(symbol)
		
