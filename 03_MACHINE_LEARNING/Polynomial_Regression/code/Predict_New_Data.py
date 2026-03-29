# =========================
# Polynomial Regression: Train, Test & Predict
# =========================

# 1️⃣ Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 2️⃣ Load Dataset
df = pd.read_csv("../data_general/product_price.csv", on_bad_lines="skip")
print("Dataset head:\n", df.head())

# 3️⃣ Define Features and Target
X = df[["advertising", "visitors"]]
y = df["sales"]

# 4️⃣ Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5️⃣ Create Polynomial Features (degree 2)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

print("X_train Polynomial:\n", X_train_poly[:5])
print("X_test Polynomial:\n", X_test_poly[:5])

# 6️⃣ Train Linear Regression Model
model = LinearRegression()
model.fit(X_train_poly, y_train)

# 7️⃣ Make Predictions on Test Set
predictions_test = model.predict(X_test_poly)

# 8️⃣ Compare Results: Actual vs Predicted
results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions_test
})
print("Comparison Test Results:\n", results.head())

# 9️⃣ Save Test Predictions
results.to_csv("output/results.csv", index=False)
print("Test results saved to output/results.csv")

# 🔟 Predict for New Customers
new_data = pd.DataFrame({
    "advertising": [350, 250, 500, 670, 750, 960, 1209],
    "visitors": [25, 20, 35, 48, 56, 65, 70]
})

# Transform new data to polynomial features
new_data_poly = poly.transform(new_data)

# Predict sales for new data
predictions_new = model.predict(new_data_poly)

# Combine new data + predictions
new_results = new_data.copy()
new_results["predicted_sales"] = predictions_new

# Save new customer predictions
new_results.to_csv("output/new_customer_prediction.csv", index=False)
print("New customer predictions saved to output/new_customer_prediction.csv")