import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Today we will learn about bar charts in matplotlib. It is used to visualize categorical data.

# Vertical bar chart:
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
runs = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
plt.bar(years, runs)
plt.title("Runs for 10 years")
plt.xlabel("Years")
plt.ylabel("Runs")
plt.xticks(years) # used to change the x-axis markings
plt.show()

# Horizontal bar chart:
players = ["Sachin", "Sehwag", "Kohli", "Yuvraj"]
runs_5yrs = [500+700+1100+1500+1800, 0+200+900 +
             1400+1600, 0+0+500+800+1100, 300+600+800+1100+900]

# y values are players and x values are runs:
plt.barh(players, runs_5yrs, color='skyblue')
plt.ylabel("Players")
plt.xlabel("Runs")
plt.show()

# Displaying values over bars:
plt.bar(players, runs_5yrs, color='green', edgecolor='k')
plt.xlabel("Players")
plt.ylabel("Runs")

# syntax: (x_coordinate, y_coordinate, text, ha = alignment_type)
for i in range(len(players)):
    # + 50 for distance between bar and text. It is done for clarity.
    plt.text(i, runs_5yrs[i] + 50, str(runs_5yrs[i]), ha='center')
plt.show()


# side-by-side bar graph:
sachin = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
sehwag = [0, 200, 900, 1400, 1600, 1800, 1500, 1100, 800, 0]
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]

# using a df:
d = {"Sachin": sachin,
     "Sehwag": sehwag,
     "Kohli": kohli}

df = pd.DataFrame(d, index=years)
print(df)
df.plot(kind='bar', legend=['Sachin', 'Sehwag', 'Kohli'])
plt.legend()
plt.show()


# using arange technique:
x = np.arange(len(years))
width = 0.25

plt.bar(x - width, sachin, width=width, label='Sachin')
plt.bar(x, sehwag, width=width, label='Sehwag')
plt.bar(x + width, kohli, width=width, label='Kohli')
plt.xticks(x, years) # for positional indexes, we have to do it like this.
plt.show()
