import matplotlib.pyplot as plt 
from ml_model_battle import test_y, pred_best

print("\nSTEP 10: Visualize Real vs Predicted")

# Use best model predictions
plt.figure()

plt.plot(list(test_y), marker='o', label="Real")
plt.plot(list(pred_best), marker='x', label="Predicted")

plt.title("Real vs Predicted (Best Model)")
plt.xlabel("Test Samples")
plt.ylabel("Score")

plt.legend()
plt.show()