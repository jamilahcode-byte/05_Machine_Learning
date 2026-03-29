# 0_1_Load_CSV_and_Libraries.py

# Import Important Libraries
import pandas as pd 
from sklearn.model_selection import train_test_split 

# Load CSV
df = pd.read_csv('sales.csv', encoding="utf-8")

# Separate Features and Target
X = df[["past_purchase", "visits_per_month"]]
y = df["target"]

print("Features (X):\n", X.head())
print("Target (y):\n", y.head())