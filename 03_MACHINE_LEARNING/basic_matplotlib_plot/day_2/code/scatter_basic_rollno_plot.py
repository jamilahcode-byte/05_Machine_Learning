import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.arange(1, 11)
y1 = x
y2 = x**2
y3 = x**3
y4 = 10*x

# Create canvas
plt.figure(figsize=(12, 8))

# First subplot (top-left)
plt.subplot(2, 2, 1)
plt.plot(x, y1, 'r-', label='y=x')
plt.title('Linear')
plt.legend()

# Second subplot (top-right)
plt.subplot(2, 2, 2)
plt.plot(x, y2, 'g--', label='y=x^2')
plt.title('Quadratic')
plt.legend()

# Third subplot (bottom-left)
plt.subplot(2, 2, 3)
plt.scatter(x, y3, color='blue', label='y=x^3')
plt.title('Cubic')
plt.legend()

# Fourth subplot (bottom-right)
plt.subplot(2, 2, 4)
plt.bar(x, y4, color='orange', label='y=10*x')
plt.title('Bar plot')
plt.legend()

# Show all plots
plt.tight_layout()  # Adjust spacing automatically
plt.show()