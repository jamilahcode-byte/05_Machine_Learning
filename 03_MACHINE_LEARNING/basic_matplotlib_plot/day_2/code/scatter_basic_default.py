#import modules 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

#style 
plt.style.use("dark_background")

#Defining the data 
rollno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
marks  = [10,20, 30, 40, 50, 60, 70, 80, 90, 100]

#Implementing Basic Scatter plot
plt.scatter(rollno, marks)
plt.show()