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

#ticks 
plt.xticks(np.arange(0, 60, 5))
plt.yticks(np.arange(10, 60, 5))

#plotting
plt.plot(temperature_pune, humidity_pune, "ro", markersize=15)

#plotting 2
plt.plot(temperature_bangalore, humidity_bangalore, 'go', markersize=15)

#Create label 
plt.xlabel("Temperature")
plt.ylabel("Humidity")

# green circles
plt.show()