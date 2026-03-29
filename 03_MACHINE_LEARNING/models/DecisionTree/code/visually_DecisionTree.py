
import matplotlib.pyplot as plt 
from DecisionTree import X, model
from sklearn import tree 

#create a draw area 
plt.figure(figsize=(12, 8))

#Draw the decision tree model 
tree.plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Not Bought", "Bought"],    filled=True,
    rounded=True,
    fontsize=10,
)
#Display the picture
plt.savefig("./visuals/tree.svg")  # scalable vector
plt.savefig("./visuals/visually_DecisionTree.jpeg")
plt.show()