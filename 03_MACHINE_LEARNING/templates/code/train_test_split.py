import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("sales.csv")
X = df[['feature1','feature2']]
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)