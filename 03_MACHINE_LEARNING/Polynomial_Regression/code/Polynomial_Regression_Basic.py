#Import Libraries
import pandas as pd 
import numpy as np 

from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures

#Load Dataset 
df = pd.read_csv("../data_general/product_price.csv", on_bad_lines="skip")
print(df.head())

#Define Features
X = df[["advertising", "visitors"]]
y = df["sales"]

#Train/Test Split
X_train, X_test,  y_train,  y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Create Polynomial Features 
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

print("X train Polynomial:\n", X_train_poly)
print("X test Polynomial:\n", X_test_poly)

#Train Model
model = LinearRegression()
model.fit(X_train_poly, y_train)

#Make Predictions
predictions = model.predict(X_test_poly)
print(f"Prediction:",predictions)

#Compare Results
results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions 
})

print(f"Compare redults:\n{results}")

#Check news customer 
new_data = pd.DataFrame({
    "advertising": [350],
    "visitors": [25]
})

# Polynomial transfer 
new_data_poly = poly.transform(new_data)

#predictions customer 
predictions = model.predict(new_data_poly)

#results
print(f"Prediction new data:{predictions}")
