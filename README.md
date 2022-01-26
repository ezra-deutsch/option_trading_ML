# option_trading_ML

![PRESENTATION HEADER](https://user-images.githubusercontent.com/88256967/151248541-d66f5b56-f1ed-409b-846a-1cc94b3f5a63.png)



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

>pip freeze >requirements.txt

[Enviornment_requirements.txt](https://github.com/ezra-deutsch/option_trading_ML/files/7945861/Enviornment_requirements.txt)



The dataset used for this project is the historical stock data for the DOW30 and all option contracts for the DOW30 as of January 6, 2022. In order to retrieve this data, yfinance api will be used.

- Download 800 option chain .csv files from API
- Loaded .csv into three PostgreSQL tables "stock_info", "stock_hist", "opt_hist_table"
- Used Pandas query the PostgreSQL database for a total of 23877 rows and 17 columns.

![Postgres-Python-Result](https://user-images.githubusercontent.com/88256967/151249195-ddfc7576-7094-4165-9e4d-4cd5ab5775eb.png)


## Pre-Processing

![Pre-Processing-Jupyter-Notebook-Notes](https://user-images.githubusercontent.com/88256967/151249025-5f6baf70-8cff-449e-a1ac-32a065ff2fa4.PNG)


## Split/Test/Train

First, the loaded dataset was split into input and output components. Next, we split the dataset so that 80 percent is used to train the model and and 20 percent is used to evaluate it. This split was choosen arbitrarily. We can then define and fit the model on the training dataset.

We seperated our dataset into our feature and target:

- Feature: Strike, Bid, Ask, Change, PercentChange, Volume, Implied Volatility, InTheMoney, Ticker, CallPut, LastTradeDate, and ExpDate.

- Target is LastPrice. (Two components that make up the price of an option are its intrinisic and time value.)

![split_train_test](https://user-images.githubusercontent.com/88256967/151249126-61875b7f-ffae-4843-ab23-5ee04f8e600f.png)


## Machine Learning

Linear regression analysis rests on the assumption that the dependent variable (y) is continuous. This makes Linear Regression Modeling the perferred method for price prediction.

![modeling_LinearRegression](https://user-images.githubusercontent.com/88256967/151249229-a39ffe9f-275a-4c8b-882c-953f132830ff.png)


## Post-Processing

After reviewing the results of our linear regression model and predicted values we merged the outputs to the original dataset.

![post_processing](https://user-images.githubusercontent.com/88256967/151249420-070bc610-7a7c-4813-a1ea-9d1b3b3a26cb.png)

## Results/Visualization

We imported our data into Tableau to be able to present a dual axis chart that plots both yhats and last price. [Click here for interactive model display](https://public.tableau.com/views/Option_Trading_ML_TableauStory/Presentation?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link).

![Tableau Screenshot](https://user-images.githubusercontent.com/88256967/151249699-7d16a394-57d6-445a-bf55-1a35c62025ef.PNG)


## Recommendation for future analysis

For future analysis other machine learning models such as Decision Tree and RandomForest may be a better option. Additional features to include would be Yield Curve Plots and Implementing greens (delta, gamma, theta, vega). This static model will be used as the foundation for future time-series modeling. 





