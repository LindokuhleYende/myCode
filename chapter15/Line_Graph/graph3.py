import matplotlib.pyplot as plt
#import numpy as np

# python  = np.array([10,8,7, 6, 1 ])
# javascript = np.array([2, 6, 5, 9, 8])
# html = np.array([1, 10, 8 ])
labels = ["Python", "Javascript", "Html", "Css"]
sizes = [50, 25,0, 25]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Favourite Languages")
plt.show()