# We will create a project of weather data analysis. We will generate random temperatures of 30 days between 20 and 40 degree Celsius. We will find it's mean, median, standard deviation, hottest and coldest days.

import numpy as np

rng = np.random.default_rng(seed=1)
temps = rng.integers(20, 40, size=30)
print(f"Temperatures: {temps}")

# Hottest day.
print(f"The hottest day: {np.argmax(temps) + 1}/06/20xx: {np.max(temps)}")

# Coldest day
print(f"The coldest day: {np.argmin(temps) + 1}/06/20xx: {np.min(temps)}")

# Average temperature
print(f"Average temperature: {np.round(np.mean(temps),1)}")

# Median temperature
print(f"Median temperature: {np.median(temps)}")

# Standard deviation
print(f"Standard deviation of temperatures: {np.round(np.std(temps), 1)}")
