#Step 1: Import Libraries 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier,  export_text, plot_tree 
from sklearn.metrics import accuracy_score, classification_report, precision_score,  recall_score 


#Load Dataset
df = pd.read_csv("../../../data_general/simple_leads.csv", on_bad_lines="skip", encoding="utf-8")
print(df.head())

#Step 3: Preprocess Data
X = df[['past_purchase','visits', 'age']].apply(lambda col: col.astype(str).str.strip().astype(int))

# Encode 'region' (categorical)
X['region'] = df['region'].str.strip()
X = pd.get_dummies(X, columns=['region'])
y = df['lead_score'].astype(str).str.strip().astype(int)

#Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#Train Decision Tree Model 
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

#Step 6: Predictions & Evaluation
predictions = model.predict(X_test)
# Save predictions for client
df_result = X_test.copy()
df_result['predicted_lead'] = predictions
df_result.to_csv("./output/predictions.csv", index=False)

print(f"Prediction: {predictions}")

#Evaluate Model 
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, zero_division=0, average='macro')
recall = recall_score(y_test, predictions, zero_division=0, average='macro')

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")

print(classification_report(
    y_test,
    predictions,
    target_names=['Cold','Medium','Hot'],
    zero_division=1   # <-- this fixes the warnings
))

new_customer = pd.DataFrame({
    "past_purchase": [350],
    "visits": [3],
    "age": [25],
    "region": ["North"]   # include region
})

# Convert region to same dummies as training
new_customer = pd.get_dummies(new_customer, columns=['region'])

# Add any missing columns (those that exist in X_train but not in new_customer)
for col in X_train.columns:
    if col not in new_customer.columns:
        new_customer[col] = 0

# Reorder columns to match training
new_customer = new_customer[X_train.columns]

prediction = model.predict(new_customer)
print("Will the customer buy?", prediction)