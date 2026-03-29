#Import Important Libraries
import pandas as pd 
from sklearn.model_selection import train_test_split 

#Load csv 
df = pd.read_csv('sales.csv',encoding="utf-8")

#Separate Features and Target
x = df[["past_purchase", "visits_per_month"]]
y = df["target"]


#Split Data into Training & Test
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

#Print Sizes
print("Training data size:", x_train.shape)
print("Test data size:", x_test.shape)
