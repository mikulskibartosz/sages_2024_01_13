from pathlib import Path
import pandas as pd
from prophet import Prophet
from prophet.serialize import model_to_json
from sklearn.metrics import mean_squared_error


if __name__ == "__main__":
    train_data = pd.read_csv("data/preprocessed/train_data.csv")
    test_data = pd.read_csv("data/preprocessed/test_data.csv")

    train_data = train_data.rename(columns={"Date": "ds", "Price": "y"})

    model = Prophet()
    model.fit(train_data)

    future = test_data[["Date"]].copy().rename(columns={"Date": "ds"})
    forecast = model.predict(future)

    actual_data = test_data["Price"].values
    predicted_data = forecast["yhat"].values

    mse = mean_squared_error(actual_data, predicted_data)
    print(f"Mean Squared Error: {mse}")

    model_path = Path("data/models/prophet")
    model_path.mkdir(parents=True, exist_ok=True)

    with open(model_path / "model.json", "w") as f:
        json_model = model_to_json(model)
        f.write(json_model)
