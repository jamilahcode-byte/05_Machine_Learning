
#Visualize the Prediction
#import modules 
from train_model import y_test, predictions 
import matplotlib.pyplot as plt 

#prapare scatter & values 
plt.scatter(y_test, predictions)

#enters values labels 
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")

#table title 
plt.title("Actual vs Predicted")

#display 
plt.show()
plt.savefig("sales_prediction.png")
print("Plot saved as sales_prediction.png")    