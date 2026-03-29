#Step 1: import modules 
import pandas as pd 
import os 

#Step 2: Load Dataset 
file_path = os.path.join("datasets","housing", "housing.csv")

#Step 3: Load data 
housing = pd.read_csv(file_path)

#Step 4: compute correctly tion matrix 
corr_matrix = housing.corr(numeric_only=True)

#Step 5: Correction with target 
corr_wity_prixe = corr_matrix["median_house_value"]

#Step 7: print results 
print(corr_width_price)

#Step 8: Sort values (highest yo lowest) 
print(corr_with_price.sort_values(ascending=False))

# Step 9: Show top 5 strongest correlations
print(corr_with_price.sort_values(ascending=False).head())