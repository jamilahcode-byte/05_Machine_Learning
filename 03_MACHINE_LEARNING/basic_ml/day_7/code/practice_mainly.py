#Step 1 import modules 
import pandas as pd 
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt 

#Step 2 create dataframe / load data    
data = pd.DataFrame({
    "Hours_Studied": [0, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9],
    "Test_Score": [2, 4, 6, 8, 12, 18, 24, 38, 46, 58, 60, 67, 69],
    "Sleep_Hours": [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7],
})

#Step 3 review & checks 
print("Review:", data.head())
print("Information\n:", data.info())
print("Checks:\n", data.describe())

#Step 4 give for plt dat

#subplot one char
plt.subplot(2,1,1)
plt.scatter(data["Hours_Studied"], data["Test_Score"])
plt.xlabel("Hours studied")
plt.ylabel("TEST SCORE")

#next charts subplot 2
plt.subplot(2,1,2)
plt.hist(data["Test_Score"], bins=7, color="skyblue", edgecolor="black")
plt.xlabel("Test Score")
plt.ylabel("Frequency")
plt.title("Histogram of Test Scores")
plt.show()

