#Step 1 import modules 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

#step 2 style uses 
plt.style.use("dark_background")

#Step 3 data 
study_hours = [2, 3, 4, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12]
marks = [6, 10, 15, 20, 34, 44, 55, 67, 70, 80, 90, 100, 100]

#Step 4 prspare scatter 
plt.scatter(study_hours, marks, color='red', s=55)

#step 5 display
plt.show()
