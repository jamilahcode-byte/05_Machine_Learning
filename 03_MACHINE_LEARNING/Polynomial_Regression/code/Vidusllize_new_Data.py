import matplotlib.pyplot as plt 
from Predict_New_Data import new_results
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # needed for 3D plotting
import pandas as pd
# Create figure and 3D axis
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot: X=advertising, Y=visitors, Z=predicted_sales
ax.scatter(new_results['advertising'], new_results['visitors'], new_results['predicted_sales'], color='blue', s=50)

# Labels
ax.set_xlabel('Advertising')
ax.set_ylabel('Visitors')
ax.set_zlabel('Predicted Sales')

# Title
ax.set_title('Polynomial Regression Predictions (3D)')

# Save & show
plt.savefig("./charts/sales_prediction_new_data_3D.png")
plt.show()



