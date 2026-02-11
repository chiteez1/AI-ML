import numpy as np

# Today we will learn to filter the data. It can be done through boolean indexing.
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])

# Selecting elements less than 5
less_5 = arr[arr < 5]
print(f"Less than 5: {less_5}")

# Selecting less than and equal to five
# Note: Always use &, |, ~ (not) operators for numpy array. It doesn't support py logical operators. Also, <= can be used too.
less_5 = arr[(arr < 5) | (arr == 5)]

print(f"Less than or equal to 5: {less_5}")

# Selecting the even nums
even = arr[arr % 2 == 0]
print(f"Even numbers: {even}")

# Note: The above methods always flatten the array. They change it's shape. In order to retain the shape, we can use:

# .where(): It maintains the shape of the array. However, it is considered slower than boolean indexing.args: condition, array_name, fill_value (The value to be filled in place of false elements).

# Selecting element >5.
great_10 = np.where(arr > 5, arr, -1)

print(f"Greater than 5:\n{great_10}")

# It retains the shape by filling the false elements - elements which don't match the condition - with fill values.
