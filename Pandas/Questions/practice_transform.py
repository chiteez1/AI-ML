import pandas as pd

# Questions:
# 1. Given this DataFrame:
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 95, 90],
    'Age': [25, 30, 22]
})
# Sort the DataFrame by Score in descending order.

df.sort_values("Score", ascending=False, inplace=True)
print(df)

# 2. Given this DataFrame:

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 95, 90]
}).set_index('Name')
# Reset the index so that Name becomes a column again.
# Reset the index but drop the old index.

df.reset_index(inplace=True) # If I drop the old index, then name is gone.
print(df)

# 3. Create a DataFrame with shuffled row indexes:
df = pd.DataFrame({
    'Value': [100, 200, 300]
}, index=['c', 'a', 'b'])

# Sort it by index alphabetically.

df.sort_index(inplace=True)
print(df)

# 4. Given:
df = pd.DataFrame({
    'First Name': ['Alice', 'Bob'],
    'Score': [85, 90]
}, index=['row1', 'row2'])

# Rename the column ‘First Name’ → ‘Name’
# Rename the index ‘row1’ → ‘student1’

df.rename(index={'row1': 'student1'},columns={'First Name': 'Name'},inplace=True)
print(df)

# 5. Reorder the columns in this DataFrame so that ‘Score’ comes first:
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Score': [85, 90],
    'Age': [25, 30]
})
df = df[['Score'] + [x for x in df.columns if x!='Score']]
print(df)
