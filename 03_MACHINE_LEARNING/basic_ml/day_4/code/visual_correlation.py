#Step 1: import modules 
import pandas as pd 
import matplotlib.pyplot as plt 
import os 

#Step 2: Load Dataset 
file_path = os.path.join("datasets","housing", "housing.csv")

#Step 3: Load data 
housing = pd.read_csv(file_path)

# Step 4: Scatter plot (income vs house price)
housing.plot(
    kind="scatter",
    x="median_income",           # input feature
    y="median_house_value",      # target
    alpha=0.1                    # transparency
)

#Title
plt.title("Income vs House Price")
plt.xlabel("Median Income")
plt.ylabel("Median House Value")


# Step 5: Show plot
plt.show()

