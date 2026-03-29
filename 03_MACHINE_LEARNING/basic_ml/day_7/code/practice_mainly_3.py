#Step 1 import modules 
import pandas as pd 
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt 

#Step 2 create dataframe / load data    
data = pd.DataFrame({
    "Hours_Studied": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Test_Score": [2, 8, 16, 33, 68, 78, 86, 88, 89, 90, 90.50],
    "Sleep_Hours": [1, 2, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]
})

X = data[["Hours_Studied", "Sleep_Hours"]]
y = data["Test_Score"]


#Step 3 review & checks 
print("Review:", data.head())
print("Information\n:", data.info())
print("Checks:\n", data.describe())

#Step 4 give for plt dat

#subplot one char
plt.subplot(2,1,1)
# Color = Sleep_Hours
plt.scatter(X["Hours_Studied"], y, c=X["Sleep_Hours"], cmap='viridis', s=100)
plt.xlabel("Hours Studied")
plt.ylabel("Test Score")
plt.title("Test Score vs Hours Studied (Color = Sleep Hours)")
plt.colorbar(label="Sleep Hours")

#next charts subplot 2
plt.subplot(2,1,2)
plt.hist(y, bins=7, color="skyblue", edgecolor="black")
plt.xlabel("Test Score")
plt.ylabel("Frequency")
plt.title("Histogram of Test Scores")
plt.show()

