#Import Important Libraries
import pandas as pd 
from sklearn.model_selection import train_test_split 

df = pd.read_csv("sales.csv")

X = df[['past_purchase','visits_per_month']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("X Train:",X_train)
print("X Test:", X_test)
print("Y Train:",y_train)
print("Y Test:", y_test)