import numpy as np

# Broadcasting in numpy: It is the process of expanding either of the array to perform operations on array with different shapes.

# Condition:
# 1. The columns and rows of the array should be same. (3,3) (3,3)
# 2. Rows and columns should contain 1 either of the array. (3,1) (1,3)
# They can satisfy either of the above condtions or both too. (3,3) (1,3)
# Note: The rows and columns with value as 1 get expanded. The normal values don't change.

# scalar
arr1 = np.array([[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10]])

print(arr1.shape)
# Expands 2 to [[2, 2, 2, 2, 2],[2, 2, 2, 2, 2]]. Here 2 is shaped like (1,1). It satisfies the condtions.
print(arr1 + 2)


# Rows
arr2 = np.array([1, 2, 3, 4, 5])
print(arr1.shape)
# It prints (5,) which is nothing but (1, 5). It satisfies the conditions.
print(arr2.shape)
print(arr1 + arr2)  # It expands arr2 to [[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]]


# Columns
arr3 = np.array([[1],
                 [2]])

arr4 = np.array([1, 2, 3])
print(arr3.shape)
print(arr4.shape)  # It is nothing but (1, 3)

'''It will expand arr3 into [[1, 1, 1],
                             [2, 2, 2]]

And arr4 into [[1, 2, 3],
               [1, 2, 3]]

The result would be:
[[2, 3, 4],
 [3, 4, 5]]
'''
print(arr3 + arr4)


# Exercise
# Task: Add vector `v` to each row of matrix `A` using broadcasting.
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
v = np.array([10, 20, 30])

# Solution:
# v will expand into [[10, 20, 30],
# [10, 20, 30],
# [10, 20, 30]]
print("Question 1:", A+v, sep='\n')

