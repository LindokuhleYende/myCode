import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#Generate random data
data = np.random.randn(1000)

#Create figure and axis
fig, ax = plt.subplots()

#Histogram data
counts, bin_edges = np.histogram(data, bins=30)

#Normalize for color mapping
colors = np.linspace(0, 1, len(bin_edges) - 1)

#Loop through each bar and add gradient effect
for i in range(len(bin_edges) - 1):
    left = bin_edges[i]
    right = bin_edges[i + 1]
    bottom = 0
    top = counts[i]

    # Create a gradient rectangle
    gradient = np.linspace(0, 1, 256).reshape(-1, 1)  # Vertical gradient
    cmap = plt.get_cmap('coolwarm')  # Choose a gradient colormap
    gradient = cmap(gradient)  # Apply colormap
    gradient = np.repeat(gradient[:, np.newaxis, :], 256, axis=1)  # Expand to RGB

    # Create an image within the histogram bar
    #ax.imshow(gradient, extent=[left, right, bottom, top], aspect='auto', alpha=0.8)

#Set labels and show the plot
ax.set_xlim(bin_edges[0], bin_edges[-1])
ax.set_ylim(0, max(counts) * 1.1)
plt.show()