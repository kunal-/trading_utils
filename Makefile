run: data/NIFTY.csv
	python bolliger_bands.py

data/NIFTY.csv: stocks_time.py
	python get_data.py

