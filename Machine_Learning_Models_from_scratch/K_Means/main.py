import numpy as np

np.random.seed(42)


# function for K-Means
def K_means(x: np.ndarray, ln: int, k: int):
    cl = np.empty((0, 2))  # list of centroids
    b_cl = np.zeros((k, 2))

    # choose random centroid
    for _ in range(k):
        rnd = np.random.randint(0, ln)
        print(f"Random: {rnd}")
        print(f"Random(x): {x[rnd]}")
        cl = np.append(cl, [x[rnd]], axis=0)
    print(f"Centroids: {cl}")

    # np.all: It's used to evaluate if all the elements in an array are True. Here, cl_1 == cl[0] returns a boolean array
    # np.array_equal: It's used to evaluate if two arrays are same and of same shape.

    # main loop
    # compare and improve centroids. Stop when centroids don't move
    # while not np.array_equal(b_cl, cl):
    while not np.allclose(b_cl, cl):
        d = {}  # dict to store clusters
        # compare
        for i in range(len(x)):
            # calculate distance
            # distance = np.sqrt((x1 - cx)**2 + (y1 - cy)**2)
            di = []
            for j in cl:
                print(f"x[i]: {x[i]}")
                print(f"j: {j}")
                di.append(np.sqrt(np.sum((x[i] - j) ** 2)))
            print(f"Di: {di}")

            # get lowest value's index
            min_di = di.index(min(di))

            # build clusters with indices
            if min_di not in d.keys():
                d[min_di] = [i]
            else:
                d[min_di].append(i)
            print(f"Dict: {d}")

        # calculate mean and change centroids
        b_cl = cl.copy()
        print(f"Old centroids: {b_cl}")
        for i in range(k):
            sum_x = 0
            sum_y = 0
            n = len(d[i])
            for j in d[i]:
                a, b = x[j]
                sum_x += a
                sum_y += b
            cl[i] = [sum_x / n, sum_y / n]
        print(f"New centroids: {cl}")
    return d


# 2 clear clusters in 2D
X = np.array(
    [
        [1, 2],
        [1.5, 1.8],
        [2, 1],
        [1.2, 2.5],
        [8, 8],
        [8.5, 8.2],
        [9, 8],
        [8, 9],
        [7.5, 8.5],
    ]
)
# a, b = K_means(X, 9, 2)
# print("For 2K:", a, b)
a = K_means(X, len(X), 2)
print(f"2K:{a}")


# 3 clusters in 2D
X = np.array(
    [
        # Cluster 1 (bottom-left)
        [1, 1],
        [1.5, 2],
        [2, 1.5],
        [1.2, 1.8],
        # Cluster 2 (top-middle)
        [5, 8],
        [5.5, 8.5],
        [6, 8],
        [5.2, 7.8],
        # Cluster 3 (bottom-right)
        [9, 2],
        [9.5, 2.5],
        [10, 2],
        [9.2, 1.8],
    ]
)
a = K_means(X, len(X), 3)
print(f"3K: {a}")
