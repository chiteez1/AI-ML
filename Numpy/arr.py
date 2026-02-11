# Today we will learn about numpy array. It is superior to python array since it is fast and we can perform multiple operations on it. That's all I really care about.
import numpy as np

# In normal list
li = list([1, 2, 3, 4, 5])
print(li * 2)  # It just reapeats the list. This is why we need a numpy array.


# This is faster.
arr = np.array([1, 2, 3, 4, 5])

# It can perform the following operations without a loop.
print(arr * 2)
print(type(arr))

# 2d array filled with "7"
arr2 = np.full((3, 3), 10)
print(f"2d array filled with 10:\n{arr2}")

# array of floats
arr3 = np.array([1, 2, 3, 4, 5], dtype="float32")
print(arr3, arr3.dtype)

# creating int array from float array
arr4 = np.astype(arr3, "int32")
print(arr4)