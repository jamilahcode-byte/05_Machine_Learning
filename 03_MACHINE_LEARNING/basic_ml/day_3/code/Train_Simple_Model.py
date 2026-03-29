from sklearn.linear_model import LinearRegression
import numpy as np

X = np.c_[data["GDP per capita"]]
y = np.c_[data["Life satisfaction"]]

model = LinearRegression()
model.fit(X, y)

print(model.predict([[22587]]))  # predict for new GDP / التنبؤ بدخل جديد