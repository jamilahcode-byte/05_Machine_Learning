#Step 1 import modules 
import numpy as np  
import sklearn.linear_model  

#Data (GDP -> happiness)
X = np.array([[12000], [27000], [37000], [50000], [55000]])
y = np.array([4.9, 5.8, 6.5, 7.3, 7.2])

#Create model 
model = sklearn.linear_model.LinearRegression()

#Train 
model.fit(X, y)

#Predict 
prediction = model.predict([[22587]])
print(f"Prediction: {np.round(prediction, 2)}")
print(f"Prediction: {np.round(model.predict([[30000]]),2)}")
print(f"Prediction: {np.round(model.predict([[10000]]),2)}")
