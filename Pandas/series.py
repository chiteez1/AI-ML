import pandas as pd

# From today, we will start learning pandas. Here we will learn series in pandas. It is very similar to 1d array in numpy.
s = pd.Series([1, 2, 3, 4, 5])
print(s)


# Change the index. Creating a series using a dict
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
s2 = pd.Series(d)
print(s2)


# Object, float and boolean series
s3 = pd.Series([x for x in 'abcd'])
s4 = pd.Series([1.2, 2.3, 3.4, 4.5, 5.6])
s5 = pd.Series([True, False, True, True])
print(s3)
print(s4)
print(s5)


# Indexing: We can use .loc[] for label-based and .iloc[] for index-based indexing.
print("First element of s2:", s2.loc['a'])
print("First element of s3:", s3.iloc[0])


# Updating the data
s2.loc['a'] = 11
print(f"First element of s2 after update: {s2.loc['a']}")
s3.iloc[0] = 'f'
print(f"First element of s3 after update: {s3.iloc[0]}")


# Slicing: Label-based and index based
print("First two elements of s2:", s2.loc['a':'b'], sep='\n') # stop value is included. Returns a series
print("First two elements of s3:", s3.iloc[0:2], sep='\n') # stop is not included. Returns a series


# Comparsion
print("Greater than 3:", s > 3, sep='\n')
print("Odd:", s % 2 != 0, sep='\n')


# Boolearn indexing
print("Greater than 3:", s[s > 3], sep='\n')
print("Odd:", s[s % 2 != 0], sep='\n')


# Homework:
li = ['bulbasaur', 'ivysaur', 'venusaur',
      'charmander', 'charmeleon', 'charizard']
s = pd.Series([x.capitalize() for x in li], index=[1, 2, 3, 4, 5, 6])
print(s)
