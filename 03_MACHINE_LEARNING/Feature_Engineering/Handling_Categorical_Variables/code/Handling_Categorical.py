import pandas as pd

df = pd.DataFrame({
    'product': ['A','B','C'],
    'category': ['Electronics','Clothing','Electronics']
})

df_encoded = pd.get_dummies(df, columns=['category'])
print(df_encoded)