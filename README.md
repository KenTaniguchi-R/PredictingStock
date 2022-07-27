# Stock Prediction

suggesting stocks which would go up tmrw using LightGBM.

suggesting from 300 tickers and collected the financial data from yfinance. In previous version, I tried to predict daily return for each, however, there are a lot of factors that affect the daily return. So instead of predicting daily return, I predict which stocks will go up. When tuning model, the score is focused on this prediction.

I added feature engineering, technical operators. However, I decided not to use most of them because they reduce score. In order to take care of time series, added lags for some columns.

Collected 10 years period, 1 day interval for each stock and split into train, validation and test data. In stock prediction, we should not use future data to train model. so I used first 70% as a train, 18% as a validation, and 12% as a test data.

Used LightGBM model because the executing time is much smaller then Random Forest or XGBOOST. When tuning, used TimeSeriesSplit for cross validation, and the maximizing score is the average daily return of the few biggest daily return.
