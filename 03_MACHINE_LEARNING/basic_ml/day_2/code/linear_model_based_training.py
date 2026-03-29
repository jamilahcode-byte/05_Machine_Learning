from sklearn.neighbors import KNeighborsClassifier

# Training data / بيانات التدريب
X = [[1], [2], [3], [4]]  # feature / الميزة
y = [0, 0, 1, 1]          # labels / التصنيفات

# Instance-based model / نموذج معتمد على الأمثلة
model = KNeighborsClassifier(n_neighbors=2)
model.fit(X, y)

# Predict new data / التنبؤ ببيانات جديدة
print(model.predict([[3.2]]))  # Output = 1 / الناتج = 1