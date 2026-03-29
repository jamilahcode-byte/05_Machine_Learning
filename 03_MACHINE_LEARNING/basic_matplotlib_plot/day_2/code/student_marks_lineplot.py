#import modules 
import seaborn as sns 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

roll_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
marks = [23, 45, 67, 89, 56, 21, 45, 67, 32, 67, 76, 32, 23, 45, 56]
#marks = list(range(1,16))

sample_df = pd.DataFrame({"Rollno": roll_no, "Marks": marks})
print(sample_df.head())

#line plot 
sns.lineplot(x= "Rollno", y= "Marks", data= sample_df)

#Title 
plt.title("Student Marks")

#show 
plt.show()