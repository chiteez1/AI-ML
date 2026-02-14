import matplotlib.pyplot as plt
import numpy as np

# 1.
days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

# Plot a stack plot with appropriate labels and legend.
# Use different colors for each activity.
plt.stackplot(days, sleeping, eating, working, playing, labels=['Sleeping', 'Eating', 'Working', 'Playing'], colors=['r', 'g', 'b', 'y'])
plt.legend(loc = 'upper left')
plt.show()


# 2.
# Modify the stack plot to:
# Add transparency (alpha) to the stack layers.
# Customize the line style (linestyle, linewidth) of the borders.
# Title the plot as "Daily Activities Over 5 Days".
# Add grid lines to the plot.
plt.title('Daily Activities Over 5 Days')
plt.stackplot(days, sleeping, eating, working, playing, labels=['Sleeping', 'Eating', 'Working', 'Playing'], colors=['r', 'g', 'b', 'y'], alpha=0.9)
plt.legend(loc='upper left')
plt.grid()
plt.show()


# 3.
# Create a stack plot from randomly generated data using numpy.random.randint.
# Each activity should have a different range (e.g., 1-3 hrs for "eating", 6-9 hrs for "sleeping", etc.).
# Include a legend, axis labels, and title.
rng = np.random.default_rng(seed=2)
sleeping = rng.integers(6,9,size=(5,))
eating = rng.integers(1,3,size=(5,))
working = rng.integers(6,8, size = (5,))
playing = rng.integers(2,4, size = (5,))

plt.title('Daily Activities Over 5 Days')
plt.stackplot(days, sleeping, eating, working, playing, labels=['Sleeping', 'Eating', 'Working', 'Playing'])
plt.xlabel("Days")
plt.ylabel("Hours")
plt.legend(loc = 'upper left')
plt.show()