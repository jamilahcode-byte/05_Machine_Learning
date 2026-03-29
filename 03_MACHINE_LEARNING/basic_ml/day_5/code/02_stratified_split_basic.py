# Import libraries
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

# Example dataset
housing = pd.DataFrame({
    "income": [1,2,3,4,5]*20,
    "price": list(range(100, 200))
})

# Create income category (IMPORTANT)
housing["income_cat"] = housing["income"]

# Create splitter
split = StratifiedShuffleSplit(
    n_splits=1,
    test_size=0.2,
    random_state=42
)

# Perform split
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

# Check distribution
print("Test set distribution:")
print(strat_test_set["income_cat"].value_counts() / len(strat_test_set))

# Remove helper column
for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)

# Final output
print("\nTrain set:")
print(strat_train_set.head())

print("\nTest set:")
print(strat_test_set.head())