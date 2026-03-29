import matplotlib.pyplot as plt 
from RF_customer_prediction import features, importance 

plt.figure(figsize=(6,4))

#make bar & add features & importance 
plt.bar(features, importance)

#add title
plt.title("Feature Importance")

#add ylabels
plt.ylabel("Importance")

#add features 
plt.xticks(rotation=30)
plt.tight_layout()

#save & display
plt.savefig("output/visualization.png")
plt.show()