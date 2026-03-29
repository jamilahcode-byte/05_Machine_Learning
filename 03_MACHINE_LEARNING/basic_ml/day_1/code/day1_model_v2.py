#import module 
import numpy as np 
from sklearn.linear_model import LinearRegression 

#Data (GDP -> happiness)
X = np.array([[12000], [27000], [37000], [50000], [55000]])
y = np.array([4.9, 5.8, 6.5, 7.3, 7.2])

#Train Model 
model = LinearRegression().fit(X ,y)

#predicts 
pred_1 = model.predict([[10000]])
pred_2 = model.predict([[30000]])


print("predictions:", pred_1, pred_2)

