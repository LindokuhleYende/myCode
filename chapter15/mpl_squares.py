import matplotlib.pyplot as plt

square = [1, 4, 9, 16, 25]
# input_values = [1, 2, 3, 4, 5]
fig, ax = plt.subplots()
# 
# plt.style.use('seaborn-v0_8')
# ax.plot(input_values, square, linewidth=3)
ax.plot(square)
plt.show()

# Set chart title and label axes.
plt.title("Square Numbers")
plt.xlabel("Value")
plt.ylabel("Square of Value")

# Set size of tick labels.
# ax.tick_params(labelsize=14)