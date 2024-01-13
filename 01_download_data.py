import pandas as pd


if __name__ == "__main__":
    URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/dowjones.csv"

    df = pd.read_csv(URL)

    print(df.head())

    df.to_csv("data/raw/dowjones.csv", index=False)
