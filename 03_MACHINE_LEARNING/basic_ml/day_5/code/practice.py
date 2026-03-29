#STEP 1 — Import tools
print("STEP 1: Import tools")

import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

print("Tools ready ✅")

#STEP 2 — Create data
print("\nSTEP 2: Create dataset")

housing = pd.DataFrame({
    "id": range(1, 24),
    "income_cat": [
        1,1,1,1,
        2,2,2,2,2,2,
        3,3,3,3,3,3,3,
        4,4,
        5,5,5,5
    ],
    #"labels": [1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
})

print("Dataset:")
print(housing)

#Count each group
print("\nSTEP 3: Count each category")

counts = housing["income_cat"].value_counts()
print(counts)

#Convert to percentage
print("\nSTEP 4: Convert to percentage")

percent = housing["income_cat"].value_counts(normalize=True)
print(percent)

#Create splitter
print("\nSTEP 5: Create smart splitter")

split = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=42)

print("Splitter ready ✅")

print("\nSTEP 6: Split and show indexes")

#Split and show indexes
for train_index, test_index in split.split(housing, housing["income_cat"]):
    print("Train index:", train_index)
    print("Test index:", test_index)

print("\nTEST DATA:")
print(housing.loc[[3,6,12,18,16]])

print("\nSTEP 7: Create train and test data")

#Create train and test sets
for train_index, test_index in split.split(housing, housing["income_cat"]):
    train_set = housing.loc[train_index]
    test_set = housing.loc[test_index]

print("Train data:")
print(train_set)

print("\nTest data:")
print(test_set)

#Check test distribution
print("\nSTEP 8: Check test distribution")
train_percent = train_set["income_cat"].value_counts(normalize=True)
test_percent = test_set["income_cat"].value_counts(normalize=True)
print(test_percent)
print(train_percent)

#Compare full vs test
print("\nSTEP 9: Compare FULL vs TEST")

print("FULL:")
print(percent)

print("\nTEST:")
print(test_percent)

#Clean data
print("\nSTEP 10: Remove helper column")

train_set = train_set.drop("income_cat", axis=1)
test_set = test_set.drop("income_cat", axis=1)

print("Clean train:")
print(train_set.head())

print("\nClean test:")
print(test_set.head())