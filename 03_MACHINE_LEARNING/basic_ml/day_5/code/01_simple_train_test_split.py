# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split

# Example dataset
housing = pd.DataFrame({
    "income": [1,2,3,4,5,1,2,3,4,5],
    "price": [100,200,300,400,500,110,210,310,410,510]
})

# Split data (random)
train_set, test_set = train_test_split(
    housing,
    test_size=0.2,
    random_state=42
)

# Print results
print("Train set:")
print(train_set)

print("\nTest set:")
print(test_set)