import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("example_data.csv")
print(data.head())  # show first 5 rows / عرض أول 5 صفوف

data.plot(kind='scatter', x='GDP per capita', y='Life satisfaction')
plt.show()