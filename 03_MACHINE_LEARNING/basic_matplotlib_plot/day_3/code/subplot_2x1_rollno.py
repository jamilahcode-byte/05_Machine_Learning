#import modules 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

#style 
plt.style.use("dark_background")

#Defining the data 
temperature_pune = [25,34,21,45,28,6,43,18,7,2]
humidity_pune = [28, 25,29,20, 26, 50, 19, 29, 52, 55]

temperature_bangalore = [34,35,36,37,28,27,26,25,31,20]
humidity_bangalore = [40, 38, 36, 35, 42, 44, 41, 40, 34, 45]

#Creating Figure & plot
plt.figure(figsize=(8, 8))

#plotting
plt.plot(temperature_pune, humidity_pune, "ro", markersize=15)

plt.plot(temperature_bangalore, humidity_bangalore, 'go', markersize=15)  # green circles
plt.show()