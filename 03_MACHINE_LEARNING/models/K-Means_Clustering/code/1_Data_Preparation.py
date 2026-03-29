# -----------------------------
# 1️⃣ Import Libraries
# -----------------------------
import pandas as pd

# -----------------------------
# 2️⃣ Load Dataset
# -----------------------------
df = pd.read_csv("customers_v2.csv", on_bad_lines="skip", encoding="utf-8")
print("First 5 rows of dataset:")
print(df.head())

# Optional: Save a copy
df.to_csv("output/customers_clean.csv", index=False)