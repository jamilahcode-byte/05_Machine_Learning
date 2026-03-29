# Step 1: Import modules
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import os


#files path
file_path = os.path.join("datasets", "housing", "housing.csv")

#Step 2: Load data 
housing = pd.read_csv(file_path)

#Step 3: Create graphics 
housing.plot(kind="scatter", x="longitude", y="latitude")

#display
plt.show()