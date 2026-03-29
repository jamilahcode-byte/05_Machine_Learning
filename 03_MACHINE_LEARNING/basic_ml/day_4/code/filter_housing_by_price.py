#import modules 
import pandas as pd 
import matplotlib.pyplot as plt 

#Step 2: Load datasets 
file_path = 'datasets/housing/housing.csv'
housing = pd.read_csv(file_path)

#Step 3: Ask the user for price range 
# Ask user for minimum and maximum house price
min_price = int(input("Enter minimum house price: "))
max_price = int(input("Enter maximum house price: "))

#Step 4: Filter dataset based on user input
# Filter rows where price is between min_price and max_price
filtered_houses = housing[
    (housing["median_house_value"] >= min_price) &
    (housing["median_house_value"] <= max_price)
]

#Step 5: Draw scatter plot for filtered houses 
filtered_houses.plot(
    kind="scatter",
    x="longitude",
    y="latitude",
    alpha=0.5,
    s=filtered_houses["population"]/100,
    c=filtered_houses["median_house_value"],
    cmap=plt.get_cmap("jet"),
    colorbar=True,
    figsize=(10,7),
    label="population"
)
plt.legend()
plt.title(f"Houses between ${min_price} and ${max_price}")
plt.show() 

#Step 6: Extra print to show how many houses matched 
