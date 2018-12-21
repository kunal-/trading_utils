run: data/NIFTY.csv
	python daily_returns.py

data/NIFTY.csv: stocks_time.py
	python get_data.py

