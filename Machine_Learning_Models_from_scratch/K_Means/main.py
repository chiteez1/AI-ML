import numpy as np

np.random.seed(42)

# function for K-Means
def K_means(x: np.ndarray, ln: int, k: int):
    cl = np.empty((0, 2))  # list of centroids
    # cl_1 = 0
    # cl_2 = 0
    b_cl = []
    # c1 = np.empty((0, 2))  # cluster 1
    # c2 = np.empty((0, 2))  # cluster 2
    d = {}

    # choose random centroid
    for _ in range(0, k):
        rnd = np.random.randint(0, ln)
        print(f"Random: {rnd}")
        print(f"Random(x): {x[rnd]}")
        cl = np.append(cl, [x[rnd]], axis=0)
    print(f"Centroids: {cl}")

    # np.all: It's used to evaluate if all the elements in an array are True. Here, cl_1 == cl[0] returns a boolean array

    # main loop
    # compare and improve centroids. Stop when centroids don't move
    # while not np.all(cl_1 == cl[0]) and not np.all(cl_2 == cl[1]):
    while not np.array_equal(b_cl, cl):
        # compare
        for i in x:
            # calculate distance
            # distance = np.sqrt((x1 - cx)**2 + (y1 - cy)**2)
            # d1 = np.sqrt((i[0] - cl[0][0]) ** 2 + (i[1] - cl[0][1]) ** 2)
            # d2 = np.sqrt((i[0] - cl[1][0]) ** 2 + (i[1] - cl[1][1]) ** 2)
            # print(f"Distance to c1: {d1}")
            # print(f"Distance to c2: {d2}")

            # # append to nearest cluster
            # if d1 < d2:
            #     print("Append to c1")
            #     c1 = np.append(c1, [i], axis=0)
            # else:
            #     print("Append to c2")
            #     c2 = np.append(c2, [i], axis=0)
            di = []
            for j in range(2):
                print(f"i[0]: {i[0]}")
                print(f"cl[j][0]: {cl[j][0]}")
                print(f"i[1]: {i[1]}")
                print(f"cl[j][1]: {cl[j][1]}")
                di.append(np.sqrt((i[0] - cl[j][0]) ** 2 + (i[1] - cl[j][1]) ** 2))
            print(f"Di: {di}")

            # get lowest value's index
            min_di = di.index(min(di))

            # group the value
            if min_di not in d.keys():
                d[min_di] = [i]
            else:
                d[min_di].append(i)
            print(f"Dict: {d}")

        # calculate mean
        b_cl = cl

        # # c1
        # sum_x = 0
        # sum_y = 0
        # n = len(c1)
        # for i in c1:
        #     a, b = i
        #     sum_x += a
        #     sum_y += b
        # # print(f"Sum_x, Sum_y, n (c1): {sum_x, sum_y, n}")
        # # cl_1 = cl[0]
        # cl[0] = [sum_x / n, sum_y / n]

        # # c2
        # sum_x = 0
        # sum_y = 0
        # n = len(c2)
        # for i in c2:
        #     a, b = i
        #     sum_x += a
        #     sum_y += b
        # # print(f"Sum_x, Sum_y, n (c2): {sum_x, sum_y, n}")
        # # cl_2 = cl[1]
        # cl[1] = [sum_x / n, sum_y / n]
        # print(f"New centroids: {cl}")

        for i in range(k):
            sum_x = 0
            sum_y = 0
            n = len(d[i])
            for j in d[i]:
                a, b = j
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
a = K_means(X, 9, 2)
print("2K:", a)
