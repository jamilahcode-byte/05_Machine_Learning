# -----------------------------
# 1️⃣ Import Libraries
# -----------------------------
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 2️⃣ Load Clustered Dataset
# -----------------------------
df = pd.read_csv("output/clustered_customers.csv")

# -----------------------------
# 3️⃣ Scatter Plot Clusters
# -----------------------------
plt.figure(figsize=(8,6))
plt.scatter(df['Purchase'], df['Visits'], c=df['cluster'], cmap='coolwarm', s=50)
plt.xlabel("Purchase")
plt.ylabel("Visits")
plt.title("Customer Segmentation (K-Means Clustering)")
plt.colorbar(label="Cluster")
plt.grid(True)
plt.tight_layout()

# -----------------------------
# 4️⃣ Save Plot & Show
# -----------------------------
plt.savefig("output/cluster_plot.png")
plt.show()