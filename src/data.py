from os import lseek
import pandas as pd
from Historic_Crypto import HistoricalData


if __name__ == "__main__":

    assets = ["BTC-USD", 'ETH-USD']
    for asset in assets:
        df = HistoricalData(asset, 86400, "2020-05-25-00-00", "2021-06-01-00-00").retrieve_data()
        df = df['close']
        df.to_csv("../inputs/train.csv")