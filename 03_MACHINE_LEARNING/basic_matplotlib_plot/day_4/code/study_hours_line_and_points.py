#import modules 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

#make style 
plt.style.use("dark_background")

#load data 
study_hours = [2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12]
marks = [6, 10, 15, 20, 34, 44, 55, 60,55, 67, 70, 80, 90, 99, 100]

#create figure 
plt.figure(figsize = (8,8))

#range tricks 
plt.xticks(np.arange(0, 15, 1))
plt.yticks(np.arange(0, 100, 5))

#plot 
plt.plot(study_hours,  marks, 'r-')
plt.plot(study_hours,  marks, 'bo')
#create labels 
plt.xlabel("Study Hours")
plt.ylabel("Marks")
#display 
plt.show()