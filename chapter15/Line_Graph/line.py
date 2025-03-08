import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9,16, 25]
fig, ax = plt.subplots()
ax.plot(input_values,squares, linewidth = 3)

#Adding title and Labeling the axes
ax.set_title("Square Numbers")
ax.set_xlabel("Value")
ax.set_ylabel("Square of Value")
ax.set_facecolor("beige")

#Add grid
plt.grid()

#Add the poits
plt.scatter(input_values, squares)
plt.show()