import matplotlib.pyplot as plt
import matplotlib as mpl
from DecisionTree import X, model
from sklearn import tree 

dpi = mpl.rcParams['figure.dpi']  # default dpi
width = 18
height = 10

#create a draw area 
plt.figure(figsize=(width, height), dpi=dpi)

#Draw the decision tree model 
tree.plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Not Bought", "Bought"],    filled=True,
    rounded=True,
    fontsize=10,
)

#Display the picture
plt.savefig("./visuals/visually_DecisionTree_v2.png")  # scalable vector
plt.savefig("./visuals/visually_DecisionTree_v2.jpeg")
plt.show()