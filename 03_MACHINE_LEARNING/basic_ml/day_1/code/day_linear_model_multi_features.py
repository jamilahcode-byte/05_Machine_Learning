import numpy as np
from sklearn.linear_model import LinearRegression

# Example Data
# GDP and Employment Rate → Happiness
X = np.array([[12000, 0.9],
              [27000, 0.95],
              [37000, 0.97],
              [50000, 0.98],
              [55000, 0.99]])
y = np.array([4.9, 5.8, 6.5, 7.3, 7.2])

# Create Model
model = LinearRegression()

# Train
model.fit(X, y)

# Predict for new country
prediction = model.predict([[22587, 0.96]])
print("Prediction:", prediction)