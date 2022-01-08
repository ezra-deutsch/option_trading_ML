# Set dependencies
import config
import yfinance as yf
import pandas as pd
import numpy as np
import os

tickers = ['AAPL','AMGN','AXP','BA','CAT','CRM','CSCO','CVX','DIS','DOW',
            'GS','HD','HON','IBM','INTC','JNJ','JPM','KO','MCD','MMM','MRK','MSFT',
            'NKE','PG','TRV','UNH','V','VZ','WBA','WMT']

for ticker in tickers:
    df = yf.Ticker(ticker).history(period='max')
    df['symbol'] = ticker
    df.to_csv(f"Resources/stock_hist/{ticker}.csv")

