#Visualize Predictions
import matplotlib.pyplot as plt
from logistic_classification import df

#Scatter & prapare 
plt.scatter(df['past_purchase'], df['visits_per_month'], c=df['bought'])

#labesl named
plt.xlabel('Past Purchase')
plt.ylabel('Visits per Month')

#titles 
plt.title('Customer Classification')
#save & display 
plt.savefig("visuals/visually_Logistic.png")
plt.show()w()