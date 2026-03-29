#Step 1 import modules 
import pandas as pd  

#Step 2 load data 
df = pd.read_csv("products.csv", on_bad_lines ="skip", encoding="utf-8")

#Step 3 (option label Encoding)
from sklearn.preprocessing import LabelEncoder 

#setup LabelEncoder 
le = LabelEncoder() 

#category encoding 
df["category_encoded"] = le.fit_transform(df['category']) 

print(df.head())

#One-Hot Encoding 
#df_encoded = pd.get_dummies(df, columns=["category"]).astype(int)
df_encoded = pd.get_dummies(df, columns=['category'], dtype=int)

print(df_encoded.head())
