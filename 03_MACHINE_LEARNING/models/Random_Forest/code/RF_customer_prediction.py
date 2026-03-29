#Import Libraries
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score,  recall_score 


#Load Dataset
df = pd.read_csv("../../data_general/customers.csv", on_bad_lines="skip", encoding="utf-8")
print(df.head())

#Define Features
X = df[['past_purchase','visits', 'ads_clicked']].apply(lambda x: x.astype(str).str.strip().astype(int))
y = df['bought'].astype(str).str.strip().astype(int)

#Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train Random Forest
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

#Make Predictions 
predictions = model.predict(X_test)
print(f"Prediction: {predictions}")

#Evaluate Model 
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, zero_division=0)
recall = recall_score(y_test, predictions, zero_division=0)

print(f"\nAccuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}\n")

#Feature Importance (Very Important) 
importance = model.feature_importances_ 
for i, v in enumerate(importance):
    print("Feature:", X.columns[i], "importance:"  , )
new_customer = pd.DataFrame({
    "past_purchase": [350,380,450],
    "visits": [3,4, 5],
    "ads_clicked": [1, 0, 1]
})

prediction = model.predict(new_customer)
print("\nWill the customer buy?", prediction)