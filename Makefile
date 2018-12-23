run: data/NIFTY.csv
	python asset_allocation.py

data/NIFTY.csv: stocks_time.py
	python get_data.py

