from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    'product': ['A','B','C'],
    'category': ['Electronics','Clothing','Electronics']
})

le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])
print(df)