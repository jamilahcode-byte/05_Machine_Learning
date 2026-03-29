import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)
y = x ** 2

plt.figure(figsize=(12, 6))  # size of the whole figure

for i in range(1, 30):
    plt.subplot(4, 9, i)  # 2 rows, 3 cols, i-th subplot
    plt.plot(x, y + i*5, marker='o')  # just to differentiate
    plt.title(f"Plot {i}")

plt.tight_layout()  # adjust spacing
plt.show()