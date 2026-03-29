import matplotlib.pyplot as plt 
from  Polynomial_Regression_Basic import y_test,predictions 

#scatter & prapare plt values 
plt.scatter(y_test, predictions)

#enter values & labels 
plt.xlabel("Actual")
plt.ylabel("Predicted")

#title
plt.title("Polynomial Regression")

#save as png & show
plt.savefig("./charts/sales_prediction.png")
plt.show()




