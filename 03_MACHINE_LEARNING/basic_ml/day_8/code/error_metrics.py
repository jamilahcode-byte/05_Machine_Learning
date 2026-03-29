#Step 1: import modules 
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np 

#Step 2: Data predictions & actually 
y_true = [156400, 120000, 180000]
y_pred = [158400, 118000, 185000]

#Step 3: RMSE
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
print(rmse)

print(np.sqrt((2000**2 + 2000**2 + 5000**2)/3))

#Step 4: MAE 
mae = mean_absolute_error(y_true, y_pred)
print(mae)
print((2000+2000+5000)/3)