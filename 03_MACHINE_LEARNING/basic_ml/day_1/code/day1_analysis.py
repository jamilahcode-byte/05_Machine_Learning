import matplotlib.pyplot as plt 
from day2_model import X, y, model

#plot to see 
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')

#best line 
plt.show()