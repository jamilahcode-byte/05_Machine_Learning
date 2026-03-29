#Step 1 import modules 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

#step 2 style uses 
plt.style.use("dark_background")

#Step 3 data 
study_hours = [2, 3, 4, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12]
marks = [6, 10, 15, 20, 34, 44, 55, 67, 70, 80, 90, 100, 100]

#prapare plot figure 
plt.figure(figsize = (8,8))

#subplot 1 
plt.subplot(2,2, 1)
plt.scatter(study_hours, marks)

#subplot 2
plt.subplot(2,2, 2)
plt.plot(study_hours, marks, 'r--')

#subplot 3
plt.subplot(2,2,3)
plt.hist(marks)

#subplot 4
plt.subplot(2,2, 4)
plt.plot(study_hours, marks, 'r--')
plt.plot(study_hours, marks, 'r--')

#saving the plot
plt.savefig('visuals/subplot.png', quality=100, facecolor = 'k')
#step 5 display
plt.show()
