#Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

#Load Dataset 
df = pd.read_csv("../../data_general/sales_probability.csv", on_bad_lines="skip", encoding="utf-8")
print(df.head())


#Define Features
X  = df[['past_purchase','visits_per_month']]
y = df['bought']  # categorical target

#Train/Test Split
X_train, X_test,  y_train,  y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train/Test Split
X_train, X_test, y_train,  y_test = train_test_split(X,  y,  test_size=0.25,  random_state=42)

#Train Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train )

#Make Predictions
predictions = model.predict(X_test)
print(predictions)

#Evaluate Model
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, zero_division=0)
recall = recall_score(y_test, predictions, zero_division=0)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

#Try classifying a new customer:
new_customer = pd.DataFrame({
    'past_purchase': [350],
    "visits_per_month": [3]
})
prediction = model.predict(new_customer)
print("Will the customer buy?", prediction)
