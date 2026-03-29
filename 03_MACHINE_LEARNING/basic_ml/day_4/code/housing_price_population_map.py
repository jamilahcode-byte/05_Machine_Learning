#Step 1: import modules 
import matplotlib.pyplot as plt 
import pandas as pd 

#Step 2: Load the dataset 
file_path = "datasets/housing/housing.csv"
house = pd.read_csv(file_path,  on_bad_lines="skip", encoding="utf-8")

#Step 3: clCreate scatter plot 
housing.plot(
    #step 4: kind of plot 
    kind="scatter",
    #Step 5: label x 
    x="Longitude",
    #Step 6: label y 
    y="Latitude",
    #Step 7: alpha
    alpha=0.5,
    #Step 8: filtered 
    s=filtered_hoises["population"]/100,
    c=filtered_hoises["median_house_value"],
    #Step 9: color map 
    cmap=plt.get_cmap("jet"),
    #Step 9: color bar 
    colorbar=True,
    #Step 10: figsize 
    figsize=(10,7),
    #Step 9: label 
    label="population"
    )
plt.legend()
plt.title(f"Houses between ${min_price} and ${max_price}")
plt.show()