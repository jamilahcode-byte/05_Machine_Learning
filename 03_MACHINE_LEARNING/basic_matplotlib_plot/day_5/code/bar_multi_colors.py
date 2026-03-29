#import modules 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

#style 
plt.style.use("dark_background")

#data 
subjects = ["Math", "English", "Science", "Social Studies", "Computer", "IT"]
marks = [89, 90, 45, 78, 99, 97]

#colors for display 
colors = ["red", "blue", "orange", "purple", "brown", "pink"]
#make bar 
plt.bar(subjects, marks, color=colors)

#display 
plt.show()