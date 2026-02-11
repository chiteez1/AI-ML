import numpy as np

# Today we will learn about aggregate functions in numpy. They take array as an input and return a single value.

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

arr2 = np.array([1, 2, 3, 4, 5])

# 1. sum(): Gives the sum of all elements in an array.
print("Sum:", np.sum(arr))

# Sums all the elements of each columns: [[1+2+3], [4+5+6]]. axis = 1 is for columns. Output : [6, 15]
print("Sum(columns):", np.sum(arr, axis=1))

# Sums all the rows [1+4, 2+5, ...]. axis = 0 is for rows. Output: [5, 7, 9]
print("Sum(rows):", np.sum(arr, axis=0))

# 2. mean: gives the avg of all the values
print("Mean:", np.mean(arr))

# 3. standard deviation
print("Standard deviation:", np.std(arr))

# 4. variance
print("Variance:", np.var(arr))

# 5. min(): prints the smallest value
print("Min:", np.min(arr))

# 6. max(): prints the highest value
print("Max:", np.max(arr))

# 7. argmin(): prints the index of min value
print("Arg-min:", np.argmin(arr))

# 8. argmax(): prints the index of max value
print("Arg-max:", np.argmax(arr))

# 9. np.prod(): product of all elements
print(f"Product of all elements: {np.prod(arr)}")

# 10. median(): median of the arr
print(f"Median: {np.median(arr)}")

# 11. np.percentile(): compute the percentile of an array
print(f"50th percentile: {np.percentile(arr, 50)}")  # For 50th percentile.

# 12. np.corrcoef(): Compute the correlation coefficient matrix of two arrays.
print(f"Correlation coefficient matrix: {np.corrcoef(arr, arr2)}") # the shape should be same

# 13. np.linspace(): Create an array of n number of elements with equal difference between each.
print(f"Linspace: {np.linspace(1, 10, 3)}")

# 14. np.log(x): Compute the natural logarithm of an array. It uses euler's number. It's like asking: "What power should we raise e to get x?"

print(f"Log(x) for base e: {np.log(arr2)}")

# 15. np.exp(x): Compute the exponential of an array. It uses euler's number too. It's like asking:
# what is e raised to  power of x or each element of the array.
print(f"Exponential for base e: {np.exp(arr2)}")
