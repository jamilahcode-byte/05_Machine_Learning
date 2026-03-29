# Step 1: Import modules
import pandas as pd
import matplotlib.pyplot as plt
import os
from pandas.plotting import scatter_matrix

# Step 2: Load data
file_path = os.path.join("datasets", "housing", "housing.csv")
housing = pd.read_csv(file_path)

# Step 3: Select important features
attributes = [
    "median_house_value",
    "median_income",
    "total_rooms",
    "housing_median_age"
]

# Step 4: Scatter matrix
scatter_matrix(housing[attributes], figsize=(10, 8))

# Step 5: Show
plt.show()