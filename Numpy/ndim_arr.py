# Today we will learn about different dimensions of np arr. We can have infinite dimensions. But we will learn upto three here.
import numpy as np

# 0 dimension
arr0 = np.array("A")  # It is like a point on a coordinate geometry graph.
print("Dimensions: ", arr0.ndim)
print("Shape:", arr0.shape)

# 1 dimension
arr1 = np.array([1, 2, 3, 4, 5])
print("Dimensions: ", arr1.ndim)
print("Shape:", arr1.shape)  # number of elements
print(arr1[0])  # Indexing

# 2 dimension
arr2 = np.array([[1, 2, 3, 4, 5],  # The number of columns must be equal. It is also called matrix.
                 [6, 7, 8, 9, 10]])

print("Dimensions:", arr2.ndim)
print("Shape:", arr2.shape)  # number of x,y

# This is called multidimensional indexing. It is same as writing [0][1].
print(arr2[0, 1])

# 3 dimension
# The number of rows and column should be equal. It is also called tensor. You can think of it as a collection of square matrices.

arr3 = np.array([[[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],

                 [[10, 11, 12],
                  [13, 14, 15],
                  [16, 17, 18]],

                 [[19, 20, 21],
                  [22, 23, 24],
                  [25, 26, 27]]])
print("Dimensions:", arr3.ndim)
print("Shape:", arr3.shape)  # number of depth,x,y.
print(arr3[0, 0, 1])

print("Exercise:")

# add any three numbers from the 3d array
total = arr3[0, 1, 1] + arr3[1, 1, 1] + arr3[2, 1, 1]
print("Sum:", total)

# reshaping a array: rows * cols should be equal. If we increase the number of rows, then it shifts the elements of the current row into the next or a new row. If we decrease the rows, then it shifts the elements from the current row to the previous rows. It is just like word wrap.

arr4 = arr2.reshape((5, 2))
print(f"Reshaped:\n{arr4}")

# flatten a nd array
arr5 = arr2.flatten() # You can arrs upto n dimensions
print(f"Flattened arr2: {arr5}")