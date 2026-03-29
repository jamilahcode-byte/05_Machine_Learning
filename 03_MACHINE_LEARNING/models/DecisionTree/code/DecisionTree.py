#Import Libraries
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score, precision_score,  recall_score 


#Load Dataset
df = pd.read_csv("../../data_general/leads.csv", on_bad_lines="skip", encoding="utf-8")
print(df.head())

X = df[['past_purchase','visits_per_month']].apply(lambda x: x.astype(str).str.strip().astype(int))
y = df['bought'].astype(str).str.strip().astype(int)

#Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

#Train Decision Tree Model 
model = DecisionTreeClassifier(max_depth=3)
model.fit(X_train, y_train)

#Make Predictions 
predictions = model.predict(X_test)
print(f"Prediction: {predictions}")

#Evaluate Model 
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, zero_division=0)
recall = recall_score(y_test, predictions, zero_division=0)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")

new_customer = pd.DataFrame({
    "past_purchase": [350],
    "visits_per_month": [3]
})

prediction = model.predict(new_customer)
print("Will the customer buy?", prediction)