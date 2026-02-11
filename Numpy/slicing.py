import numpy as np

# Slicing is the process of obtaining a small part of an array or list in the same form.
# one-dimension slicing
a = np.array([1, 2, 3, 4, 5])
print(a[1:5])

# two dimensional slicing
a2 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]])

print(a2[0:2])  # first two rows
print(a2[:, 0:2])  # first two columns
print(a2[:-3:-1])  # reverse last two rows
print(a2[:, ::-1])  # reverse columns
print(a2[:2, :2])  # top left quadrant.
print(a2[1:, 2:])  # bottom right quadrant.

# three dimension slicing
a3 = np.array([[[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]],

               [[13, 14, 15, 16],
                [17, 18, 19, 20],
                [21, 22, 23, 24],],

               [[25, 26, 27, 28],
                [29, 30, 31, 32],
                [33, 34, 35, 36]]])

print(a3[:, 0, 0])  # first element of every matrix
print(a3[:,:,0]) # first column
print(a3[:,:,::-1]) # reverse the array
print(a3[0:2,0:2,0:2]) # top left quadrant of first two matrices. Returns a 3d array.

# Declaration with slicing
a3[:,:,0] = 1
print(a3)
