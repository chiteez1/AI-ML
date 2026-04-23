import numpy as np

# function for K-Means
def K_means(x: np.ndarray, ln: int, k: int):
    cl = np.empty((0, 2))  # list of centroids
    c1 = np.empty((0, 2))  # cluster 1
    c2 = np.empty((0, 2))  # cluster 2

    # choose random centroid
    for _ in range(0, k):
        rnd = np.random.randint(0, ln)
        print(f"Random: {rnd}")
        print(f"Random(x): {x[rnd]}")
        cl = np.append(cl, [x[rnd]], axis=0)
    print(f"Centroids: {cl}")

    # compare
    for i in x:
        # calculate distance
        # distance = np.sqrt((x1 - cx)**2 + (y1 - cy)**2)
        d1 = np.sqrt((i[0] - cl[0][0]) ** 2 + (i[1] - cl[0][1]) ** 2)
        d2 = np.sqrt((i[0] - cl[1][0]) ** 2 + (i[1] - cl[1][1]) ** 2)
        print(f"Distance to c1: {d1}")
        print(f"Distance to c2: {d2}")
        # append to nearest cluster
        if d1 < d2:
            print("Append to c1")
            c1 = np.append(c1, [i], axis=0)
        else:
            print("Append to c2")
            c2 = np.append(c2, [i], axis=0)

    # calculate mean
    # c1
    sum_x = 0
    sum_y = 0
    n = len(c1)
    for i in c1:
        x, y = i
        sum_x += x
        sum_y += y
    # print(f"Sum_x, Sum_y, n (c1): {sum_x, sum_y, n}")
    cl[0] = [sum_x / n, sum_y / n]

    # c2
    sum_x = 0
    sum_y = 0
    n = len(c2)
    for i in c2:
        x, y = i
        sum_x += x
        sum_y += y
    # print(f"Sum_x, Sum_y, n (c2): {sum_x, sum_y, n}")
    cl[1] = [sum_x / n, sum_y / n]
    print(f"New centroids: {cl}")
    return c1, c2


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
a, b = K_means(X, 9, 2)
print(a, b)
