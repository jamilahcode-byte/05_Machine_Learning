# =========================
# FULL ML DATA PREPARATION
# =========================

# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

# -------------------------
# Step 1: Create dataset
# -------------------------
np.random.seed(42)

housing = pd.DataFrame({
    "median_income": np.random.randint(1, 6, 100),
    "house_price": np.random.randint(100000, 500000, 100)
})

# -------------------------
# Step 2: Create income categories
# -------------------------
housing["income_cat"] = pd.cut(
    housing["median_income"],
    bins=[0,1.5,2.5,3.5,4.5,6],
    labels=[1,2,3,4,5]
)

# -------------------------
# Step 3: Stratified Split
# -------------------------
split = StratifiedShuffleSplit(
    n_splits=1,
    test_size=0.2,
    random_state=42
)

for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

# -------------------------
# Step 4: Compare distributions
# -------------------------
def income_distribution(data):
    return data["income_cat"].value_counts() / len(data)

print("Full dataset distribution:")
print(income_distribution(housing))

print("\nStratified test set distribution:")
print(income_distribution(strat_test_set))

# -------------------------
# Step 5: Clean data
# -------------------------
for dataset in (strat_train_set, strat_test_set):
    dataset.drop("income_cat", axis=1, inplace=True)

# -------------------------
# Step 6: Final output
# -------------------------
print("\nTrain set sample:")
print(strat_train_set.head())

print("\nTest set sample:")
print(strat_test_set.head())