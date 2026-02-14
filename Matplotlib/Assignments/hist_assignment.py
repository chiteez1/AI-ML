import matplotlib.pyplot as plt
import numpy as np

# 1.
# Create a list of test scores for 30 students (you can just make up random numbers between 0 and 100).
# Plot a histogram of the scores.
# Use 10 bins.
# Add a title and labels for the x-axis ("Score") and y-axis ("Number of Students").

rng = np.random.default_rng(seed=3)
marks = rng.integers(0, 100, size=30)
plt.title("Scores of 30 students")
plt.hist(marks, 10, edgecolor='k')
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()


# 2.
# Plot a histogram of this data.
# Use 5 bins.
# Customize the bar color and add grid lines.

data = rng.integers(1, 50, size=100)
plt.hist(data, bins=5, color='red', edgecolor = 'k')
plt.grid(alpha = 0.6)
plt.show()


# 3.
# Plot a horizontal histogram (orientation='horizontal').
# Use 5 bins.
# Change the bar color to orange and add black edges.
# Add a title and axis labels.

ages = [12, 17, 19, 24, 30, 22, 45, 37, 29, 31, 34, 40, 15, 18, 21, 25, 50, 55, 60, 65]
plt.title("Age distribution")
plt.hist(ages, bins=5, color="#F29E02FF", edgecolor = 'k', orientation='horizontal')
plt.ylabel("Ages")
plt.xlabel('Frequency')
plt.show()