import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Today we will learn about seaborn. It is used to create beautiful graphs very easily. It is built on top of matplolib. Thus, matplotlib can be used for customising the plots. It works best with dataframes.

# set style:
sns.set_theme(style='dark')

# line plot:
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
runs = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]

data = pd.DataFrame({
    'years': years,
    'runs': runs
})

sns.lineplot(x='years', y='runs', data=data)
plt.xticks(data['years'])
plt.show()


# bar plot
sns.barplot(x='years', y='runs', data=data)
plt.show()


# histogram:
ages = [
    34, 28, 36, 45, 27, 27, 45, 37, 25, 35,
    25, 25, 32, 10, 12, 24, 19, 33, 20, 15,
    44, 27, 30, 15, 24, 31, 18, 33, 23, 27,
    23, 48, 29, 19, 38, 17, 32, 10, 16, 31,
    37, 31, 28, 26, 15, 22, 25, 40, 33, 12,
    33, 26, 23, 36, 40, 39, 21, 26, 33, 39,
    25, 28, 18, 18, 38, 43, 29, 40, 33, 23,
    33, 45, 29, 45, 3, 38, 30, 27, 30, 10,
    27, 33, 44, 24, 21, 24, 39, 33, 24, 35,
    30, 39, 22, 26, 26, 15, 32, 32, 30, 27
]

bins = [10, 20, 30, 40, 50, 60, 70]  # for custom bins
data = pd.DataFrame({'ages': ages})
sns.histplot(x='ages', bins=bins, data=data)
plt.show()


# box plot:
# load a seaborn dataset:
tips = sns.load_dataset('tips')
sns.boxplot(x='total_bill', y='tip', data=tips)
plt.show()

# scatter plot:
sns.scatterplot(x='years', y='runs', data=data)
plt.show()