# STEP 1: Import tools
print("STEP 1: Import tools")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

print("Tools ready ✅")


# STEP 2: Create MORE DATA
print("\nSTEP 2: Create bigger dataset")

data = pd.DataFrame({
    "age": [15,16,15,17,18,19,20,21,22,23,24,25],
    "study_hours": [2,3,1,4,5,6,7,8,6,5,7,9],   # NEW FEATURE
    "score": [80,90,70,85,88,92,95,97,96,94,98,99]
})

print(data)


# STEP 3: Check distribution
print("\nSTEP 3: Check basic info")
print(data.describe())


# STEP 4: Better split
print("\nSTEP 4: SPLIT DATA (better)")

X = data[["age", "study_hours"]]   # better features
y = data["score"]

train_X, test_X, train_y, test_y = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("Train size:", len(train_X))
print("Test size:", len(test_X))


# STEP 5: MODEL 1 (Linear)
print("\nSTEP 5: Linear Regression")

model1 = LinearRegression()
model1.fit(train_X, train_y)

pred1 = model1.predict(test_X)

mse1 = mean_squared_error(test_y, pred1)

print("Predictions:", pred1)
print("MSE Linear:", mse1)


# STEP 6: MODEL 2 (Better model)
print("\nSTEP 6: Decision Tree")

model2 = DecisionTreeRegressor(random_state=42)
model2.fit(train_X, train_y)

pred2 = model2.predict(test_X)

mse2 = mean_squared_error(test_y, pred2)

print("Predictions:", pred2)
print("MSE Tree:", mse2)



# STEP 7: Compare models
print("\nSTEP 7: COMPARE MODELS")

print("Linear MSE:", mse1)
print("Tree MSE:", mse2)

if mse1 < mse2:
    print("✅ Linear model is better")
else:
    print("✅ Decision Tree is better")



# STEP 8: Show real vs predicted
print("\nSTEP 8: REAL vs PREDICTED")

print("Real:", list(test_y))
print("Linear Pred:", pred1)
print("Tree Pred:", pred2)