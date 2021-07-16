# CointegratedPairsTrading

## Objective
Use the Engle-Granger Test: Method for checking if Bitcoin (BTC) and Ethereum (ETH) two series are cointegrated
1. Get hedge ratio from linear regression 
2. Calculate spread and check if the spread is stationary (if the spread is stationary, the two series are cointegrated)
3. Augmented Dickey-Fuller Test, if P-value <=0.05: assume spread is stationary and therefore two time-series are cointegrated

## Steps for Mean Reversion 
1.	Pair of assets that have some economic link
2.	Compute the hedge ratio
3.	Use the hedge ration to compute the spread
4.	Test if the spread is stationary
5.	If its stationary, it’s a candidate for Mean Reversion Trading
6.	Choose Threshold for the spread 
7.	When the spread Widens/Narrows its historical average short/long the spread
8.	Backtest your model 

## Code
- `main.py`: Calculating hedge-ratio and Augmented Dickey-Fuller Unit Root test.
- `data.py`: Collect historical price data for Bitcoin and Ethereum
- `config.py`: Define paths global variable 
- `plot.py`: Plot ETH/BTC price-ratio

## Data
[Collecting Coinbase API](https://developers.coinbase.com/)
- `BTCUSD`: Bitcoin
- `ETHUSD`: Ethereum 
