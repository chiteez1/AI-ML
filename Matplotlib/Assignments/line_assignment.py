import matplotlib.pyplot as plt
import numpy as np

# Assignment:
# Create a plot comparing Kohli, Rohit Sharma, and Sehwag across 10 years of hypothetical runs.
# Use:

# Labels
# Legends
# Colors
# Line styles
# One custom style


rng = np.random.default_rng(seed=1)
rohit = rng.integers(500, 2000, size=(10,))
kohli = np.array([0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100])
sehwag = np.array([0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0])
years = np.array([1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010])

plt.style.use('dark_background')
plt.title("Kohli, Sehwag, and Rohit's scores")
plt.xlabel("Years")
plt.ylabel("Runs")
plt.plot(years, kohli, color='r', linestyle=':', label='Kohli', linewidth = 2)
plt.plot(years, sehwag, color='g', linestyle='--', label='Sehwag', linewidth = 2)
plt.plot(years, rohit, color='b', linestyle='-.', label='Rohit', linewidth = 2)
plt.legend()
plt.grid()
plt.show()
