import pandas as pd 
from sklearn.model_selection import train_test_split 

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

# Features (X) and Label (y)
X = data[["Hours_Studied", "Sleep_Hours"]]
y = data["Test_Score"]

print("Features:\n", X.head())
print("Label:\n", y.head())

from sklearn.model_selection import train_test_split

# 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

# Guess value = average of training labels
guess_value = y_train.mean()
print("Guessed Test Score:", guess_value)

# Calculate simple difference (error) for test set
errors = y_test - guess_value
print("Errors:\n", errors)

# Optional: absolute error or mean error
abs_errors = abs(errors)
mean_error = abs_errors.mean()
print("Mean Absolute Error:", mean_error)