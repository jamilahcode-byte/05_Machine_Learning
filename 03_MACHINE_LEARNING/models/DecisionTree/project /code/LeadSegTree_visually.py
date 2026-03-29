import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,  export_text, plot_tree 
from LeadSegTree import model, X

# Step 1: Visualize Decision Tree
plt.figure(figsize=(20,12))
plot_tree(model,
          feature_names=X.columns,
          class_names=['Cold','Medium','Hot'],
          filled=True,
          rounded=True,
          fontsize=10)
plt.savefig("./output/decision_tree.png", dpi=300)  # scalable vector for client
plt.show()

# Step 2: Predict new customer
# Make sure new_customer has all columns after dummy encoding
new_customer = pd.DataFrame({
    "past_purchase": [350],
    "visits": [3],
    "age": [28],
    "region_East": [0],
    "region_North": [1],
    "region_South": [0],
    "region_West": [0]
})

prediction = model.predict(new_customer)
print("Will the customer buy?", prediction)  # 0=Cold, 1=Medium, 2=Hot