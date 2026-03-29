import matplotlib.pyplot as plt
from stratified_split_demo import train_percent,percent_full,  test_percent

categories = [1,2,3,4,5]  # your income categories

plt.figure(figsize=(10,5))
plt.bar([x-0.2 for x in categories], percent_full, width=0.2, label='Full')
plt.bar(categories, train_percent, width=0.2, label='Train')
plt.bar([x+0.2 for x in categories], test_percent, width=0.2, label='Test')

plt.xlabel("Income Category")
plt.ylabel("Proportion")
plt.title("Category Proportion: Full vs Train vs Test")
plt.xticks(categories)
plt.legend()
plt.show()