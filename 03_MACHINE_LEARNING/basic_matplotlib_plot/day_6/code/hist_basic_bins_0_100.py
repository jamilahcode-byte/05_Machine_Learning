#import modules 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

#style 
plt.style.use("dark_background")

#data
bins = np.arange(0, 100, 5)
marks_50_students = np.random.randint(0, 100, (50))

#create figure 
plt.figure(figsize = (8,8))

#plot hist
plt.hist(marks_50_students, bins=bins, color="orange", orientation="horizontal")
plt.xticks(np.arange(0, 100, 5))

plt.show()