#import library 
import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import accuracy_score,  precision_score,  recall_score 

#load data 
df = pd.read_csv("../../../data_general/customer_behavior.csv", on_bad_lines="skip", encoding="utf-8")
print(df.head())

#Create Target (IMPORTANT )
df["bought"] = df["purchases"].apply(lambda x: 1 if x >= 1 else 0)

#Features 
X = df[['visits','purchases','ads_clicked']].copy()  # <- copy
X.loc[:, 'region'] = df['region']  # <- safe assignment
X = pd.get_dummies(X, columns=['region'])
y = df["bought"]

#Train/Test Split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 

#Train Random Forest 
model = RandomForestClassifier (n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#Make Predictions
predictions = model.predict(X_test)
# Correct: probability of buying (class 1)
probabilities = model.predict_proba(X_test)[:, 1]  # this is 1D now

#Save Predictions for Client 
df_result = X_test.copy()
df_result['prediction'] = predictions
df_result['probability'] = probabilities
df_result.to_csv("output/predictions.csv", index=False) 

#Evaluate Model 
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, zero_division=0)
recall = recall_score(y_test, predictions, zero_division=0) 
 
#Feature Importance Report (Text) 
importance = model.feature_importances_
features = X.columns

with open("output/feature_importance_report.txt", "w") as f:
    f.write("Feature Importance Report\n\n")
    for i, v in enumerate(importance):
        line = f"{features[i]}: {round(v,3)}\n"
        print(line)
        f.write(line)