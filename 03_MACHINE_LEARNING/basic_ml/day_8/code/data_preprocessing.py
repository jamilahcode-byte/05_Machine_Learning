import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load
url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
housing = pd.read_csv(url)

# Fix missing
housing = housing["total_bedrooms"].fillna(housing["total_bedrooms"].median())

# Encode categorical
housing = pd.get_dummies(housing, columns=["ocean_proximity"])
print(housing.shape)

# Scale
scaler = StandardScaler()
housing_scaled = scaler.fit_transform(housing)

print("Data ready ✅")
print(housing.head())
print(housing)