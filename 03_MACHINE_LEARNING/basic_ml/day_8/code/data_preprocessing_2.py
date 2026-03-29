import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load
url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
housing = pd.read_csv(url)

# Fix missing (WITHOUT replacing dataset)
housing["total_bedrooms"] = housing["total_bedrooms"].fillna(
    housing["total_bedrooms"].median()
)

#  Encode ONLY categorical column
housing = pd.get_dummies(housing, columns=["ocean_proximity"])

# 🔍 Check shape
print("Shape after encoding:", housing.shape)

#  Scale
scaler = StandardScaler()
housing_scaled = scaler.fit_transform(housing)

#  Convert back to DataFrame
housing_scaled = pd.DataFrame(housing_scaled, columns=housing.columns)

print("Data ready ✅")
print(housing_scaled.head())