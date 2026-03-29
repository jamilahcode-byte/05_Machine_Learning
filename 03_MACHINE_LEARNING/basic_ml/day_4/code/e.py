from pandas.plotting import scatter_matrix 
import pandas as pd 
import matplotlib.pyplot as plt 

#Step 2: Load datasets 
file_path = 'datasets/housing/housing.csv'
housing = pd.read_csv(file_path)


attributes = ["median_house_value", "median_income", "total_rooms",
 "housing_median_age"]
 
scatter_matrix(housing[attributes], figsize=(12, 8))

plt.show()