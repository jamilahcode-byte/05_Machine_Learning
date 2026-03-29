#import Tools
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Load Dataset
df = pd.read_csv('../data/simple_sales.csv', encoding="utf-8")
print(df.head())

#Define Features & Target
X = df[["past_purchase", "visits_per_month"]]
y = df["sales"]

#Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train Linear Regression Model 
model = LinearRegression().fit(X_train, y_train)

#Make Predictions
predictions = model.predict(X_test)
print("Prediction Test X:\n", predictions)

#Compare Prediction vs Real Value
comparison = pd.DataFrame({
    "Actual": y_test,
    "predicted": predictions
})
print(comparison)


new_customer = pd.DataFrame({
    "past_purchase": [350],
    "visits_per_month": [3]
})

prediction = model.predict(new_customer)

prediction = model.predict(new_customer)

print("Predicted sales:", prediction)