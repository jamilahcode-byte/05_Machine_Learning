#import modules 
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 

#style 
#plt.style.use("dark_background")

#data
classes = ["Math", "English", "Science", "AI", "IT"]
marks = [80, 95, 75, 40, 65]
colors = ["red", "blue", "green", "#9803fc", "#03c2fc"]
explode_values = [0.1, 0.1, 0, 0.2, 0]

#create plot pie
plt.pie(marks, labels=classes, colors=colors, autopct="%0.2f%%", explode=explode_values, shadow=True)

plt.show()