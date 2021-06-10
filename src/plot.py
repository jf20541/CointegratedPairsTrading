import matplotlib.pyplot as plt
import config
import pandas as pd


df = pd.read_csv(config.TRAINING_FILE)


def plot_pr(data):
    price_ratio = df["ETH"] / df["BTC"]
    price_ratio.plot(figsize=(15, 8))
    plt.axhline(price_ratio.mean(), color="red")
    plt.title("ETH/BTC Price Ratio")
    plt.ylabel("Price-Ratio")
    plt.xlabel("Days")
    plt.legend(["ETH/BTC Price-Ratio", "Average Price-Ratio"])
    plt.savefig("../plots/CoinPR.jpg")
    plt.show()
    print(f"Average Price-Ratio: {price_ratio.mean():.4f}")


plot_pr()
