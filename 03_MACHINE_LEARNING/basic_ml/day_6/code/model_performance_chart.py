import matplotlib.pyplot as plt 
from ml_model_battle import results, 

print("\nSTEP 9: Visualize model comparison")

# Prepare data
model_names = list(results.keys())
mse_values = list(results.values())

# Create bar chart
plt.figure()
plt.bar(model_names, mse_values)

plt.title("Model Comparison (MSE)")
plt.xlabel("Models")
plt.ylabel("MSE (Lower is Better)")

plt.show()