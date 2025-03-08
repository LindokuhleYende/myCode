import matplotlib.pyplot as plt

x_values = range(-220, 300)
y_values = [x**3 for x in x_values]
fig, ax = plt.subplots()
ax.plot(x_values, y_values, color="yellow")
ax.set_title("Cubic Function")
ax.set_xlabel("X-Values")
ax.set_ylabel("Y-Values")
ax.set_facecolor("blue")
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds)
plt.grid()
plt.show()
