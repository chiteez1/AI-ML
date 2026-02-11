import numpy as np

# Today we will learn about random number generation in numpy.
# random number generator instance. It is used to generate random numbers.
# you can use seed keyword to preserve the random numbers. None is default value.
rng = np.random.default_rng(seed=None)
print("Random number between 1 and 5:", rng.integers(1, 6))

# Generating a 1d array of random nums.
arr = rng.integers(1, 6, size=4)
print("Array of random ints:", arr)

# Generating a matrix of random numbers.
arr2 = rng.integers(low=1, high=10, size=(3, 3))
print("Matrix of random ints:", arr2, sep='\n')


# Float numbers: We can use .uniform() to generate random floats.
print("Random floats between 1.0 and 2.0:", rng.uniform(1.0, 2.0))

# Generating a 1d array of random floats.
arr3 = rng.uniform(1.0, 2.0, size=3)
print("Array of random floats:", arr3)

# Generating a 2d array of random floats
arr4 = rng.uniform(low=1.0, high=2.0, size=(2, 2))
print("Matrix of random floats:", arr4, sep='\n')


# Random choice: We can use rng to perform a random choice over an array.
arr5 = np.array([x for x in "अआइईउऊञण"])
print("Random choice:", rng.choice(arr5))

# Array of random choice: Returns an array of randomly selected elements.
arr8 = rng.choice(arr5, size=3)
print("Array of random choice:", arr8)


# Matrix of random choice: It returns a matrix of randomly chosen elements from the array.
arr7 = rng.choice(arr5, size=(2, 3))
print("Matrix of random choice:", arr7, sep='\n')


# Shuffling an array: We all know the meaning of "shuffle". It places the elements of the array on random indices less than len(arr).
arr6 = np.array([1, 2, 3, 4, 5])
rng.shuffle(arr6)  # Modifies the array.
print(f"Shuffled array: {arr6}")


# Seeds: seed can be used to store the random numbers generated during the program. So that in the next excution they won't get random again.
