import numpy as np

# Numpy arithmetic operations
# Scalar operation: A scalar is nothing but an individual number
# Addition: Adds scalar to every element
arr = np.array([1, 2, 3, 4, 5])
print("Scalar addition:", arr + 1)

# Subtraction
print("Scalar subtraction:", arr - 2)

# Mutiplication
print("Scalar multiplcation:", arr * 2)

# Division
print("Scalar division:", arr / 2)

# Exponent
print("Raised to power of scalar:", arr**2)


# Math functions in numpy: Applies a function to every element of the array.
arr2 = np.array([3.5, 7.8, 1.0, 4.1, 6.4])

# 1. sqrt
print("Square root:", np.sqrt(arr2))

# 2. round()
# round up: round to the next integer
# round down: round to the previous integer.

# rounds to the nearest integer. In case of .5, rounds up if the next integer is even or rounds down. This is called bankers' rounding
print("round():", np.round(arr2))

# 3. floor()
print("floor():", np.floor(arr2))  # rounds down

# 4. ceil()
# rounds up. Numbers with .0 are an exception since they are already an integer.
print("ceil():", np.ceil(arr2))

# Mathematical constants
print(np.pi)


# Exercise: Calculate area of circle.
radii = np.array([1, 2, 3, 4, 5])
print("Area of a circle:", np.pi * (radii ** 2))


# Operation on two arrays
arr3 = np.array([1, 2, 3, 4, 5])
arr4 = np.array([6, 7, 8, 9, 10])
print("Addition:", arr3 + arr4)
print("Subtraction:", arr4 - arr3)
print("Multiplication:", arr3 * arr4)
print("Division:", arr3 / arr4)
print("Raised to the power:", arr3 ** arr4)

# Comparison operators
arr5 = np.array([10, 20, 30, 40, 50])
print("Greater than 20:", arr5 > 20)
print("Lesser than 40:", arr5 < 40)
print("Equal to 50:", arr5 == 50)

# Boolean indexing
print("Lesser than 40:", arr5[arr5 < 40])
print("Greater than 20:",arr5[arr5 > 20])

# Boolean assignment
arr5[arr5 % 20 == 0] = 0 # Sets all the matching values to 0
print(arr5)

arr5[arr5 == 50] = 5
print(arr5)
