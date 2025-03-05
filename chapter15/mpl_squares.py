import matplotlib.pyplot as plt

square = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(square)
plt.show()

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)