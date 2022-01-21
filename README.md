# option_trading_ML

IMAGE[URL-SLIDE-1-TBA]

## Overview

Data analytics is an integral part of almost every industry today. These days It is hard to think of an industry in which Data Analytics does not play a major role. The derivatives market, one of the stock market's greatest opportunies is not an exception. Within the derivatives market, our focus is on Stock Options which some would say is the one of the most rewarding and challenging topics. Rewarding because who does not want to earn profits in the stock market. Challenging because the length and breadth of this topic is infinite. You can easily get lost and overwhelmed with the amount of information that you can find when exploring this topic. 

As a team, we decided to study and analyze option's contract price for the DOW30, which represents 30 of the most highly capitalized and influential companies in the U.S. economy which further acts as an indicator of the market.

The goal of our project is to use Machine Learning to predict the last price of an option contract.

Our focus will be on using Machine Learning to predict the price of an option contract.

### Questions we would like to answer

What is the predicted price for each DOW30 stock option contract?

What could we have done differently, to get better results?

What do we recommend for future analysis?

## Environment and Setup

To set up the development enviornment create a new enviornment from the environment-ee.yml file

>conda env create -f environment-ee.yml

The dataset used for this project is the historical stock data for the DOW30 and all option contracts for the DOW30 as of January 6, 2022. In order to retrieve this data, yfinance api will be used.

- Download 800 option chain .csv files from API
- Loaded .csv into three PostgreSQL tables "stock_info", "stock_hist", "opt_hist_table"
- Used Pandas query the PostgreSQL database for a total of 23877 rows and 17 columns.

## Pre-Processing

Fill missing values with '0'
preprocessed_df.fillna(value=0, inplace=True)

Change 'inTheMoney' from boolean to float64
preprocessed_df['inTheMoney'] = preprocessed_df['inTheMoney'].astype('float')

Change 'lastTradeDate' to datetime64
preprocessed_df['lastTradeDate'] = pd.to_datetime(preprocessed_df['lastTradeDate'])

Change 'exp_date' to datetime64
preprocessed_df['exp_date'] = pd.to_datetime(preprocessed_df['exp_date'])

Split 'lastTradeDate' into separate components, as int64
preprocessed_df['lastTradeDate_month'] = preprocessed_df['lastTradeDate'].dt.month
preprocessed_df['lastTradeDate_day'] = preprocessed_df['lastTradeDate'].dt.day
preprocessed_df['lastTradeDate_year'] = preprocessed_df['lastTradeDate'].dt.year
preprocessed_df['lastTradeDate_hour'] = preprocessed_df['lastTradeDate'].dt.hour
preprocessed_df['lastTradeDate_min'] = preprocessed_df['lastTradeDate'].dt.minute

Split 'exp_date' into separate components, as int64
preprocessed_df['exp_date_month'] = preprocessed_df['exp_date'].dt.month
preprocessed_df['exp_date_day'] = preprocessed_df['exp_date'].dt.day
preprocessed_df['exp_date_year'] = preprocessed_df['exp_date'].dt.year
preprocessed_df

Drop columns 
preprocessed_df.drop(['contractSymbol','lastTradeDate','exp_date','contractSize','currency','company'], axis=1, inplace=True)

Create our features
Convert string columns to numbers and drop 'lastPrice' column then assign to X
X = pd.get_dummies(preprocessed_df, columns=['ticker', 'call_put',]).drop('lastPrice', axis=1)

## Split/Test/Train

First, the loaded dataset was split into input and output components. Next, we split the dataset so that 80 percent is used to train the model and and 20 percent is used to evaluate it. This split was choosen arbitrarily. We can then define and fit the model on the training dataset.

We seperated our dataset into our feature and target:

- Feature: Strike, Bid, Ask, Change, PercentChange, Volume, Implied Volatility, InTheMoney, Ticker, CallPut, LastTradeDate, and ExpDate.

- Target is LastPrice. (Two components that make up the price of an option are its intrinisic and time value.)


## Machine Learning

Linear regression analysis rests on the assumption that the dependent variable (y) is continuous. This makes Linear Regression Modeling the perferred method for price prediction.


Results of our Linear Regression Model:

- Mean Absolute Error: 3.6817083420866012
- Mean Squared Error: 89.43335730553159
- Root Mean Squared Error: 9.456921132458048
- R^2 Coefficient of Determination: 0.9782108916254928


## Post-Processing

After reviewing the results of our linear regression model and predicted values we merged the outputs to the original dataset.





