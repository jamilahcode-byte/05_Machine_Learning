# Step 1: Import modules
import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 2: Load data
file_path = os.path.join("datasets", "housing", "housing.csv")
housing = pd.read_csv(file_path)

# Step 3: Create new features
housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"] / housing["total_rooms"]
housing["population_per_household"] = housing["population"] / housing["households"]

# Step 4: Correlation
corr_matrix = housing.corr(numeric_only=True)
corr_with_price = corr_matrix["median_house_value"]

print("New correlations:\n")
print(corr_with_price.sort_values(ascending=False))

# Step 5: Plot
housing.plot(kind="scatter", x="rooms_per_household", y="median_house_value", alpha=0.1)

plt.title("Rooms per Household vs Price")
plt.show()