#STEP 1: Import tools
print("STEP 1: Import tools")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

print("Tools ready ✅")


#STEP 2: Create BIGGER DATA (MORE FEATURES)
print("\nSTEP 2: Create dataset with more features")

data = pd.DataFrame({
    "age": [15,16,15,17,18,19,20,21,22,23,24,25],
    "study_hours": [2,3,1,4,5,6,7,8,6,5,7,9],
    "sleep_hours": [6,7,5,6,7,8,7,6,7,8,6,7],
    "work_hours": [1,2,1,2,3,3,4,4,3,2,4,5],
    "happiness": [6,7,5,7,8,9,8,7,8,9,7,8],
    "score": [80,90,70,85,88,92,95,97,96,94,98,99]
})

print(data)


# STEP 3: Check data
print("\nSTEP 3: Data info")
print(data.describe())


# STEP 4: Split data
print("\nSTEP 4: Split data")

X = data[["age", "study_hours", "sleep_hours", "work_hours", "happiness"]]
y = data["score"]

train_X, test_X, train_y, test_y = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print("Train size:", len(train_X))
print("Test size:", len(test_X))


# STEP 5: Define models
print("\nSTEP 5: Create models")

models = {
    "Linear": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42),
    "KNN": KNeighborsRegressor()
}


# STEP 6: Train + Predict + Evaluate
print("\nSTEP 6: Train and evaluate models")

results = {}

for name, model in models.items():
    print(f"\n--- {name} ---")
    
    model.fit(train_X, train_y)
    pred = model.predict(test_X)
    
    mse = mean_squared_error(test_y, pred)
    results[name] = mse
    
    print("Predictions:", pred)
    print("MSE:", mse)


# STEP 7: Compare all models
print("\nSTEP 7: Compare ALL models")

for name, mse in results.items():
    print(f"{name} MSE: {mse}")

best_model = min(results, key=results.get)

print(f"\n🏆 BEST MODEL: {best_model}")


# STEP 8: Real vs Best Model
print("\nSTEP 8: Real vs Best Model")

best = models[best_model]
pred_best = best.predict(test_X)

print("Real:", list(test_y))
print("Best Predictions:", pred_best)