import matplotlib.pyplot as plt
import numpy as np
 
x = np.array([1,2,3,4,5])
square = np.array([1, 4, 9, 16, 25])
plt.plot(x, square)
# input_values = [1, 2, 3, 4, 5]
# fig, ax = plt.subplots()

# plt.style.use('seaborn-v0_8')
# ax.plot(input_values, square, linewidth=3)
plt.show()

# Set chart title and label axes.
plt.title("Square Numbers")
plt.xlabel("Value")
plt.ylabel("Square of Value")

# Set size of tick labels.
# ax.tick_params(labelsize=14)