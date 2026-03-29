from sklearn.preprocessing import OneHotEncoder, StandardScaler

encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(df[['category']])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['feature1','feature2']])