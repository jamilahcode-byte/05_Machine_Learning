#Step 1 import modules 
print("STEP 1: Import tools")

import pandas as pd 
from sklearn.model_selection import train_test_split 

print("Tools ready ✅️")

#Step 2: Create datasets
print("\nSTEP 2: Create dataset")
data = pd.DataFrame ({
    "age":[15, 16, 15, 17, 18, 19, 20, 21],
    "score": [80, 90, 70, 85, 88, 92, 95, 97]
})
print(data)

#Step 3: Split data
print("\nSTEP 3: SPLIT DATA")
train_set, test_set = train_test_split(
    data,
    test_size=0.25,
    #stratify=data["age"]
    random_state=42
    )
print("Train data:")
print(train_set)
print("Test data:")
print(test_set)

#Step 4: Train model
from sklearn.linear_model import LinearRegression 

model = LinearRegression().fit(train_set[["age"]], train_set[["score"]])

#Step 5: Test model 
print("\nSTEP 4: TEST MODEL PREDICTIONS")
predictions = model.predict(test_set[["age"]])
print(predictions)

#Step 3 measures errors
print("\nSTTP 5: ERROR measure l")
from sklearn.metrics import mean_squared_error 

error = mean_squared_error(test_set["score"], predictions)
print(error)