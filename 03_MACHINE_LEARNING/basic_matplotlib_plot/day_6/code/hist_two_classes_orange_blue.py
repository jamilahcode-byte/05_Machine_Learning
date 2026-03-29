#import modules 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

#style 
plt.style.use("dark_background")

#data
bins = np.arange(0, 100, 5)
marks_50_students_1 = np.random.randint(0, 100, (50))
marks_50_students_2 = np.random.randint(0, 100, (50))

#create figure 
plt.figure(figsize = (8,8))

#plot hist
plt.hist([marks_50_students_1, marks_50_students_2], bins=bins, color=["orange", "blue"])

plt.xticks(np.arange(0, 100, 5))
plt.xlabel("Marks")
plt.ylabel("Frequency")

#title 
plt.title("Marks of students 2 classes")


plt.show()