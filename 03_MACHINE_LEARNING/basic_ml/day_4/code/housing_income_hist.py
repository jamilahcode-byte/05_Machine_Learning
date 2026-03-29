# Step 1: Import modules
import pandas as pd
import os


#files path
file_path = os.path.join("datasets", "housing", "housing.csv")

#Step 2: Load data 
housing = pd.read_csv(file_path)

housing["income_cat"] = pd.cut(housing["median_income"],
 bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
 labels=[1, 2, 3, 4, 5])
 
housing["income_cat"].hist()