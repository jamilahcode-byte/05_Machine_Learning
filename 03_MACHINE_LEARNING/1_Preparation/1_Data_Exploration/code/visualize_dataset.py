#import modules
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("sales.csv")

#plot scatter & prapare
plt.scatter(df["past_purchase"], df["visits_per_month"], c=df["target"])

#make labels 
plt.xlabel("Past Purchase")
plt.ylabel("Visits per Month")

#write title 
plt.title("Customer Data Overview")

#display
plt.show()

