from sklearn.linear_model import LinearRegression
import numpy as np

# Training data / بيانات التدريب
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])  # target = 2 * input / الهدف = 2 * المدخل

# Batch training / التدريب دفعة واحدة
model = LinearRegression()
model.fit(X, y)

# Predict / التنبؤ
print(model.predict([[5]]))  # Output = 10 / الناتج = 10