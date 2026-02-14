import pandas as pd
import matplotlib.pyplot as plt

# Create a side-by-side bar chart comparing runs of Sachin, Kohli, and Sehwag over 5 selected years.
# Then create a horizontal bar chart showing total runs scored in their debut 5 years.

years = [1990, 1992, 1994, 1996, 1998]
d = {"Sachin": [500, 700, 1100, 1500, 1800],
     "Kohli": [0, 200, 900, 1400, 1600],
     'Sehwag': [0, 0, 500, 800, 1100]}
df = pd.DataFrame(d, index=years)
df.plot(kind='bar', legend=list(df.columns))
plt.title("Runs of Sachin, Kohli, and Sehwag")
plt.xlabel('Years')
plt.ylabel("Runs")
plt.legend()
plt.tight_layout()
plt.show()


# horizontal:
runs_5yrs = [500+700+1100+1500+1800, 0+0+500+800+1100, 0+200+900+1400+1600]
plt.barh(['Sachin', 'Kohli', 'Sehwag'], runs_5yrs)
plt.title("Total runs of Sachin, Kohli, and Sehwag")
plt.ylabel('Players')
plt.xlabel("Runs")
plt.tight_layout()
plt.show()
