import pandas as pd
import os

HOUSING_PATH = os.path.join("datasets", "housing")

def load_house_data(path=HOUSING_PATH):
    csv_path = os.path.join(path, "housing.csv")
    return pd.read_csv(csv_path)

data = load_house_data(path=HOUSING_PATH)

print("Review rows:\n", data.head())
print("\nInformation data:")
print(data.info())
print("\nDescription data:\n", data.describe())