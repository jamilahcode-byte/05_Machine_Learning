#import modules 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

#style 
plt.style.use("dark_background")

#data
classes = ["Math", "English", "Science", "AI", "IT"]
marks = [80, 95, 75, 40, 65]

#create plot pie
plt.pie(marks, labels=classes)

plt.show()