#import modules 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

#style 
plt.style.use("dark_background")

#data 
subjects = ["Math", "English", "Science", "Social Studies", "Computer", "IT"]
marks = [89, 90, 45, 78, 99, 97]

#make bar 
plt.bar(subjects, marks)

#display 
plt.show()