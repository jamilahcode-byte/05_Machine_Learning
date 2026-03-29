# Step 1: Import modules
import numpy as np
import pandas as pd

# Step 2: Friendly function to split data
def split_data(dataset, test_fraction=0.2, seed=42):
    """Split a dataset into train and test sets."""
    
    # Step 2a: Set random seed
    np.random.seed(seed)
    
    # Step 2b: Shuffle row indices
    shuffled = np.random.permutation(len(dataset))
    
    # Step 2c: Test set size
    test_size = int(len(dataset) * test_fraction)
    
    # Step 2d: Split indices
    test_idx = shuffled[:test_size]
    train_idx = shuffled[test_size:]
    
    # Step 2e: Select rows
    train = dataset.iloc[train_idx]
    test = dataset.iloc[test_idx]
    
    return train, test

# Step 3: Example dataset (all columns same length)
example_data = pd.DataFrame({
    "feature1": range(1, 11),       # length 10
    "feature2": range(11, 21),      # length 10
    "label": ["A", "B"] * 5         # length 10 ✅
})

# Step 4: Split into train and test
train_set, test_set = split_data(example_data, test_fraction=0.3)

# Step 5: Print results
print("Train set:")
print(train_set)
print("\nTest set:")
print(test_set)

# Step 6: Print sizes
print("\nNumber of rows in train set:", len(train_set))
print("Number of rows in test set:", len(test_set))