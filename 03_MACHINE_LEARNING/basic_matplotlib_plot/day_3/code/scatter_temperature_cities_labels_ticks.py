import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
df = pd.read_csv('./IRIS.csv')  # replace with your path

# Step 2: Display first 50 rows
print(df.head(50))  # head(n) shows first n rows

# Step 3: Scatter plot example (optional)
plt.scatter(df['sepal_length'], df['petal_length'])

#create labels
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')

#add title
plt.title('Sepal vs Petal Length')

#display 
plt.show()
