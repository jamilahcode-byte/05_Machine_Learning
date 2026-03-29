#import modules 
import numpy as np      
import matplotlib.pyplot as plt      
from sklearn.linear_model import LinearRegression 

#data 
X = np.array([[12000], [27000], [37000], [50000], [55000], [60000], [65000]])    
y = np.array([4.9, 5.8, 6.5, 7.3, 7.2, 7.5, 8])

#model 
model = LinearRegression()      
model.fit(X, y) 

#predictions 
X_new = np.array([[12000], [37500], [60000], [75000]])
       
predictions = model.predict(X_new) 

plt.scatter(X, y, color='blue', label='Actual Data')      
plt.plot(X, model.predict(X), color='red', label='Best Fit Line')      
plt.scatter(X_new, predictions, color='green', label='New Predictions')  
    
plt.xlabel('GDP')      
plt.ylabel('Happiness')     

#plt.legend()   
plt.savefig("gdp_happiness_plot.png")  # saves the graph as PNG   
plt.show()