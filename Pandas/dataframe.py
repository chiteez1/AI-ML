import pandas as pd
import numpy as np
import sqlite3

# Here, we will learn about dataframe. A dataframe is a structure in pandas which resembles a table. It's two dimenisonal and has rows and columns.

# Creating dataframe from dictionary of lists.
d = {"Name": ['Aman', 'Bapu', 'Cazole', 'Deep'],
     "Marks": [10, 20, 30, 40]}

# default index is 0, 1, 2 ...
df = pd.DataFrame(d, index=['a', 'b', 'c', 'd'])
print(df)

# Creating from numpy arrays
arr = np.array([['Aman', 10],
                ['Bapu', 20],
                ['Cazole', 30],
                ['Deep', 40]])

df = pd.DataFrame(arr, index=['a', 'b', 'c', 'd'], columns=["Name", "Marks"])
print(df)

# creating from csv files:
df = pd.read_csv("file_name.csv")

# creating from excel files:
df = pd.read_excel("file_name.xlxs")

# creating from json file:
df = pd.read_json("file_name.json")

# creating from sql lite database:
conn = sqlite3.connect("mydb.sqlite")
df = pd.read_sql("SELECT * FROM users", conn)

# creating df from url:
df2 = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")
print(df2)


# Label indexing
# returns a series. The column name becomes the index.
print(f"First student's marks:\n{df.loc['a']}")


# Position indexing
print(f"Second student's marks:\n{df.iloc[1]}")


# Adding a new column
df['Roll no'] = [1, 2, 3, 4]
print(f"New column:\n{df}")


# Adding a new row
df.loc["e"] = ['Elie', 50, 5]
print(f"New row:\n{df}")


# Adding multiple rows: We can do this through a new dataframe
d = {"Name": ["Falco", "Graphite"], "Marks": [60, 70], "Roll no": [6, 7]}
df3 = pd.DataFrame(d, index=['f', 'g'])

# pd.concat(): Pandas function to concat two dataframes. Syntax: (df to be concatenated, df to be concatenated from)
df = pd.concat([df, df3])
print(f"Added multiple rows:\n{df}")

# exploratory data analysis: It refers to quickly exploring the data set. It taking a quick view of the data set. We can do this through following functions:

# 1. df.head(): print first n no. of rows. default value of n is 5
print("First five columns:", df2.head(), sep='\n')

# 2. df.tail(): print last n no. of rows. default value of n is 5
print("Last five columns:", df2.tail(), sep='\n')

# 3. df.info(): gives info about the dataframe
df2.info()

# 4. df.describe(): calculates the essential stats values such as mean, std etc. of the dataframe.
print(f"Describe:\n{df2.describe()}")

# 5. df.columns: returns the list of column names.
print(f"Column names: {df2.columns}")

# 6. df.shape: returns the no. of rows, columns in tuple form
print(f"Shape: {df2.shape}")
