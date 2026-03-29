import matplotlib.pyplot as plt
from RF_customer_prediction import model, X

# Feature importance
importance = model.feature_importances_
features = X.columns

#Draw bar chart
plt.figure(figsize=(6,4))
plt.bar(features, importance, color=['skyblue','orange','green'])

#Add titles
plt.title("Feature Importance for Predicting Customer Buying")
plt.ylabel("Importance (0-1 scale)")

#dispkay
plt.savefig("visuals/visually_Random_Forest.png")
plt.show()