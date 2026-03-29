
# STEP 1 — Import tools
print("STEP 1: Import tools")
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
print("Tools ready ✅")

# STEP 2 — Create dataset
print("\nSTEP 2: Create dataset")
housing = pd.DataFrame({
    "id": range(1, 24),
    "income_cat": [
        1,1,1,1,
        2,2,2,2,2,2,
        3,3,3,3,3,3,3,
        4,4,
        5,5,5,5
    ]
})
print(housing)

# STEP 3 — Show dataset shape
print("\nSTEP 3: Dataset size")
print("Rows:", len(housing))
print("Columns:", len(housing.columns))

# STEP 4 — Count each category
print("\nSTEP 4: Count each category")
counts = housing["income_cat"].value_counts()
print(counts)

# STEP 5 — Convert to percentage
print("\nSTEP 5: Convert to percentage")
percent = housing["income_cat"].value_counts(normalize=True)
print(percent)

# STEP 6 — Create splitter
print("\nSTEP 6: Create splitter")
split = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=42)
print("Splitter ready ✅")

# STEP 7 — Generate indexes
print("\nSTEP 7: Generate indexes")
for train_index, test_index in split.split(housing, housing["income_cat"]):
    print("Train index:", train_index)
    print("Test index:", test_index)

# STEP 8 — Show example test rows manually
print("\nSTEP 8: Example test rows")
print(housing.loc[test_index])

# STEP 9 — Create train/test sets
print("\nSTEP 9: Create train/test sets")
for train_index, test_index in split.split(housing, housing["income_cat"]):
    train_set = housing.loc[train_index]
    test_set = housing.loc[test_index]

# STEP 10 — Show train data
print("\nSTEP 10: Train data")
print(train_set)

# STEP 11 — Show test data
print("\nSTEP 11: Test data")
print(test_set)

# STEP 12 — Check test distribution
print("\nSTEP 12: Test distribution")
test_percent = test_set["income_cat"].value_counts(normalize=True)
print(test_percent)

# STEP 13 — Check train distribution
print("\nSTEP 13: Train distribution")
train_percent = train_set["income_cat"].value_counts(normalize=True)
print(train_percent)

# STEP 14 — Compare FULL vs TEST
print("\nSTEP 14: Compare FULL vs TEST")
print("FULL:")
print(percent)
print("\nTEST:")
print(test_percent)

# STEP 15 — Clean dataset
print("\nSTEP 15: Clean dataset")
train_set = train_set.drop("income_cat", axis=1)
test_set = test_set.drop("income_cat", axis=1)

print("Clean train:")
print(train_set.head())
print("\nClean test:")
print(test_set.head())


# Full dataset percentages
percent_full = housing['income_cat'].value_counts(normalize=True)