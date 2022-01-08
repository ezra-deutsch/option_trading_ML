# Set dependencies
import yfinance as yf
import pandas as pd
import numpy as np
import os
import datetime

tickers = ['AAPL','AMGN','AXP','BA','CAT','CRM','CSCO','CVX','DIS','DOW',
            'GS','HD','HON','IBM','INTC','JNJ','JPM','KO','MCD','MMM','MRK','MSFT',
            'NKE','PG','TRV','UNH','V','VZ','WBA','WMT']

for ticker in tickers:
    exp_dates = yf.Ticker(ticker).options
    for date in exp_dates:
        try:
            opt_call_df = yf.Ticker(ticker).option_chain(date).calls
            split = opt_call_df['contractSymbol'].str.split(r'\d+',expand=True)
            ticker_sym = split[0]
            call_put = split[1]
            opt_call_df['ticker']=ticker_sym
            opt_call_df['call_put']=call_put
            opt_call_df['exp_date'] = opt_call_df['contractSymbol'].str.split('C').str[0]
            opt_call_df['exp_date'] = opt_call_df['exp_date'].str.extract('(\d+)',expand=False)
            opt_call_df['exp_date'] = pd.to_datetime(opt_call_df['exp_date'],yearfirst=True)
            opt_call_df.to_csv(f"Resources/opt_calls/{ticker}_calls_{date}.csv", index=False)
        except ValueError:
            print(f"No Call Option Chain for {ticker}_{date}")
        except AttributeError:
            print(f"AttributeError for {ticker}_{date}")