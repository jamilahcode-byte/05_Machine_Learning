# Step 1: Import modules
from sklearn.model_selection import train_test_split 
import pandas as pd
import os


#files path
file_path = os.path.join("datasets", "housing", "housing.csv")

#Step 2: Load data 
housing = pd.read_csv(file_path)

#Step 3: train & Test 
train_test = train_test_split(housing, test_size=0.2, train_size=0.8, random_state=42)

#Step 4: divide train & Test 
train, test = train_test

print("\nTrain data:\n", train)
print("\nTest data:\n", test)
