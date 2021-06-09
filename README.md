# CointegratedPairsTrading

## Goal
Use the Engle-Granger Test: Method for checking if two series are cointegrated
1. Get hedge ratio from linear regression 
2. Calculate spread and check if the spread is stationary (if the spread is stationary, the two series are cointegrated)
3. Augmented Dickey-Fuller Test, if P-value <=0.05: assume spread is stationary and therefore two stocks are cointegrated


## Steps to verify Mean Reversion 

1.	Pair of assets that have some economic link
2.	Compute the hedge ratio
3.	Use the hedge ration to compute the spread
4.	Test if the spread is stationary
5.	If its stationary, it’s a candidate for Mean Reversion Trading
6.	Choose Threshold for the spread 
7.	When the spread Widens/Narrows its historical average short/long the spread
8.	Backtest your model 

### Code

Created 4 modules
- `config.py`: Define paths global variable 
- `main.py`: Calculating hedge-ratio and Augmented Dickey-Fuller Unit Root test.
- `data.py`: Collect historical price data for Bitcoin and Ethereum
- `plot.py`: Plot ETH/BTC price-ratio

### Install
Install the following Python libraries

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [Scikit-Learn](https://scikit-learn.org/stable/)
- [Statsmodel](https://www.statsmodels.org/stable/index.html)
- [Historic-Crypto](https://pypi.org/project/Historic-Crypto/)


### Run

In a terminal or command window, navigate to the top-level project directory `CointegratedPairsTrading/` (that contains this README) and run the following command:

```bash
pip install --upgrade pip && pip install -r requirements.txt
``` 

## Data
[Collecting Coinbase API](https://developers.coinbase.com/)

- `BTCUSD`: Bitcoin
- `ETHUSD`: Ethereum 
