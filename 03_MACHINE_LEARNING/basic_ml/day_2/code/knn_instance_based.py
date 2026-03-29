from sklearn.linear_model import LinearRegression
import numpy as np

# Training data / بيانات التدريب
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

# Model-based training / التدريب المعتمد على النموذج
model = LinearRegression()
model.fit(X, y)

# Predict new data / التنبؤ ببيانات جديدة
print(model.predict([[5]]))  # Output = 10 / الناتج = 10