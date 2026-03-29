import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("sales.csv")

X = df[['past_purchase','visits_per_month']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# plot training data
plt.scatter(
    X_train['past_purchase'],
    X_train['visits_per_month'],
    c=y_train
)

plt.xlabel("Past Purchase")
plt.ylabel("Visits per Month")
plt.title("Customer Pattern (Training Data)")

plt.show()