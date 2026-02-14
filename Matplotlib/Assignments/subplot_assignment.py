import matplotlib.pyplot as plt
import numpy as np

# 1.
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Calculate y values for each function
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)


# Use plt.subplots() to create a 2x2 grid of subplots.
# Plot the following:
# A sine wave in the first subplot (axs[0, 0])
# A cosine wave in the second subplot (axs[0, 1])
# A tangent wave in the third subplot (axs[1, 0])
# Leave the fourth subplot (axs[1, 1]) empty.
# Set an appropriate title for each subplot.
# Add an overall title for the figure: "Trigonometric Functions"
# Adjust spacing between subplots to avoid overlap.

# Bonus:
# Set the figure size to 10x6 inches.
# Add a grid to each of the three plots.

y_values = [y_sin, y_cos, y_tan]
titles = ["Sin wave", "Cos wave", "Tan wave"]
fig, axs = plt.subplots(2, 2, figsize=(10, 6))
fig.suptitle("Trigonometric functions")
for i in range(2):
    for j in range(2):
        if i + j != 2:
            idx = i * 2 + j
            axs[i][j].plot(x, y_values[idx])
            axs[i][j].set_title(titles[idx])
            axs[i][j].grid()
plt.tight_layout()
plt.show()
