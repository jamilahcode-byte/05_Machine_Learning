#import modules 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

#style 
plt.style.use("dark_background")

#data 
subjects = ["Math", "English", "Science", "Social Studies", "Computer", "IT"]
marks1 = [89, 90, 45, 78, 99, 97]
marks2 = [78, 56, 34, 90, 12, 15]

#create a figure 
plt.figure(figsize = (8,8))


#make bar 
plt.bar(subjects, marks1)
plt.bar(subjects, marks2)

plt.xlabel("Subjects")
plt.ylabel("Marks")

#display 
plt.show()