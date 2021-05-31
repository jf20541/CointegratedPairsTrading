import pandas as pd
from Historic_Crypto import HistoricalData


if __name__ == "__main__":
    btc = HistoricalData(
        "BTC-USD", 86400, "2016-05-25-00-00", "2021-05-23-00-00"
    ).retrieve_data()
    btc = btc["close"]
    eth = HistoricalData(
        "ETH-USD", 86400, "2016-05-25-00-00", "2021-05-23-00-00"
    ).retrieve_data()
    eth = eth["close"]
    df = pd.concat([btc, eth], axis=1)
    df.to_csv("../inputs/train.csv")
