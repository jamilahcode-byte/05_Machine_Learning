import pandas as pd
from sklearn.preprocessing import StandardScaler  

df_encoded = pd.get_dummies(df, columns=['category'])
print(df_encoded)

#Feature Scaling / Normalization

#encoding category 
X = df_encoded[['category_Electronics']]

scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X)
print(X)

#Creating New Features
df['avg_purchase_per_month'] = df['total_purchase'] / df['months_active']


#Practical ML Example 
# Original features
X = df[['past_purchase','visits_per_month','category_Electronics']]

# Add new feature
X['avg_purchase'] = df['total_purchase'] / df['months_active']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)