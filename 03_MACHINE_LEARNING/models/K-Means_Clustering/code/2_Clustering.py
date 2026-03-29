#Import Libraries
import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier 
from sklearn.preprocessing import StandardScaler

#Load Dataset
df = pd.read_csv("../../data_general/customers_v2.csv", on_bad_lines="skip", encoding="utf-8")
print(df.head())

#Scale Features (Optional but Recommended)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['Purchase','Visits']])
print("Features scaled.")

#Create K-Means Model
model = KMeans(n_clusters=2, random_state=42)
model.fit(X_scaled)

#Assign Clusters 

df['cluster'] = model.labels_
print("Clusters assigned:")
print(df.head())


#save
df.to_csv("output/clustered_customers.csv", index=False)
pront("✅️ File saved successfully")