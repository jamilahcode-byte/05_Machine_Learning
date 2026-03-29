#import modules 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

#style 
plt.style.use("dark_background")

#data
marks_50_students = np.random.randint(0, 100, (50))

#plot hist
plt.hist(marks_50_students)

plt.show()