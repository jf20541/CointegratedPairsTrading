import pandas as pd 
import config
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt


df = pd.read_csv(config.TRAINING_FILE)
ETH = df['ETH'].values.reshape(-1,1)
BTC = df['BTC'].values.reshape(-1,1)

def hedge_ratio(dv, iv):
    """
    Calculating Hedge Ratio from LinearRegression Model (Slope)
    """
    lr = LinearRegression()
    lr.fit(dv,iv)
    hedge_ratio = lr.coef_[0][0]
    intercept = lr.intercept_[0]
    return hedge_ratio, intercept


def spread_adf():
    """
    Spread: linear combination of two series with a hedge ratio
    (H0): Have statioary timeseries and hence a cointegrated pair
    (H1): Not H0
    """
    spread = (ETH-BTC) * hedge_ratio(BTC, ETH)[0]
    result = adfuller(spread)
    if result[1] <= 0.05:
        print(f"Spread is Stationary and P-value: {result[1]}")
    else:
        print(f"Spread is Not Stationary: P-value: {result[1]}")

        
if __name__ == '__main__':
    spread_adf()
