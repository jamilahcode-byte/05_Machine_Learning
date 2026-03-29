#import modules 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#make style 
plt.style.use("dark_background")

#load data 
rollno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
marks = [10,20, 30, 40, 50, 60, 70, 80, 90, 100]

#plot 
plt.plot(rollno,  marks,  'r-')

#display 
plt.show()