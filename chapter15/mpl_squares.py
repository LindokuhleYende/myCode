import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([1, 4, 9,16,25])

plt.plot(x, y)

plt.title("Square Numbers")
plt.xlabel("Value")
plt.ylabel("Square of values")

plt.show()