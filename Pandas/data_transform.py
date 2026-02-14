import pandas as pd

# Today we will learn how to change the shape of our df and transform it.

df = pd.read_csv("data.csv")
print(df)

# 1. df.sort_values(): used to sort the rows using column values.
# Sort values by year:
print(df.sort_values("Year"))

# sort values by year in descending order:
print(df.sort_values("Year", ascending=False))

# We can see in the output that, some rows have same year and thus it's a tie. To counter these, we can use multiple columns:
print(df.sort_values(["Year", "IMDb"]))
# First it will sort by years and in case of any ties, it will sort by IMDb.


# 2. reset_index(): reset the index of the dataframe.
df2 = df.sort_values(['Year', "IMDb"])
df2.reset_index(drop=True, inplace=True)
print(df2)
# Here, drop is used so that it doesn't create a new column for old indices. inplace = True alters the original df2. It is present in most of the methods.

# 3. sort_index(): sort the df according to its indices. It is useful when the indices are not in sorted order.
print(df.sort_index(ascending=False))


# 4. rank(): used to rank the values. It is just like ranking students: 1st, 2nd, 3rd etc.
df["Rank"] = df["IMDb"].rank(ascending=True)
# If ascending = False; the highest number will get the lowest rank.
print(df)
# Here, in case of ties, it gives the average of both the values. If we want to give same rank for same values:
df["Rank"] = df["IMDb"].rank(method="dense")
print(df)


# 5. .rename(): this is very easy. It is used to rename column names and row indices.
print(df.rename({x: x.lower() for x in df.columns}, axis=1))

# 6. Changing column order: We can change order of columns:
df = df[['Actor', 'Film', 'Year', 'Genre',
         'IMDb', 'BoxOffice(INR Crore)', 'Rank']]
print(df)

# you can do this to bring one column to the first:
df = df[['Film'] + [x for x in df.columns if x != 'Film']]
print(df)

