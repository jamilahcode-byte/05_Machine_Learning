#import modules 
import matplotlib.pyplot as plt 
import pandas as pd 

#files path
file_path = os.path.join("datasets", "housing", "housing.csv")

#load the csv
house = pd.read_csv(file_path)

#make hist
house.hist(bins=50, figsize=(20, 15))

#display
plt.show()