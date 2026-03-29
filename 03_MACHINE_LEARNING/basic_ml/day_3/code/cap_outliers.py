#import modules 
import numpy as np 
import pandas as pd 

#create dataframe 
data = pd.DataFrame({
    "size": [50, 60, 70, 80, 1000],
    "price": [100, 120, 140, 160, 10000]
})

#compute the 95 percent 
cap_size = np.percentile(data['size'], 95)
cap_price = np.percentile(data['price'], 95)

print(f"Cap size:\n {cap_size}")
print(f"Cap price:\n {cap_price}")

#Replace outliers with the cap
data["size"] = np.where(data['size'] > cap_size, cap_size,  data['size'])
data["price"] = np.where(data['price'] > cap_price, cap_price,data['price'] )

# Rooms per household
data["rooms_per_household"] = data["size"] / 10  # simple example
print(data)

#check it
print(data)

