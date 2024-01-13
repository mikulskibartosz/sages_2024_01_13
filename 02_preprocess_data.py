import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

if __name__ == "__main__":
    data = pd.read_csv("data/raw/dowjones.csv")

    train_data, test_data = train_test_split(
        data, test_size=0.2, random_state=42, shuffle=False
    )

    print(train_data.head())
    print(test_data.head())

    normalizer = StandardScaler()

    normalizer.fit(train_data[["Price"]])

    train_data[["Price"]] = normalizer.transform(train_data[["Price"]])
    test_data[["Price"]] = normalizer.transform(test_data[["Price"]])

    pd.DataFrame(train_data).to_csv("data/preprocessed/train_data.csv", index=False)
    pd.DataFrame(test_data).to_csv("data/preprocessed/test_data.csv", index=False)

    with open("data/preprocessed/normalizer.pkl", "wb") as f:
        pickle.dump(normalizer, f)
