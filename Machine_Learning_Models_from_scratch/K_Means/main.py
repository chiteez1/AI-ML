import numpy as np

np.random.seed(42)

# Model class
class KMeans:
    def __init__(self, k: int, max_i: int) -> None:
        self.k = k
        self.i = max_i
        pass

    # function to generate random centroids
    def rand_centroid(self, x: np.ndarray) -> np.ndarray:
        cl = np.empty((0, 2))  # list of centroids
        ln = len(x)

        # choose random centroid from x
        for _ in range(self.k):
            rnd = np.random.randint(0, ln)
            cl = np.append(cl, [x[rnd]], axis=0)
        return cl

    # training function
    def fit(self, x: np.ndarray) -> dict[int, np.ndarray]:
        # start with random
        cl = self.rand_centroid(x)

        # main loop
        # compare and improve centroids. Stop after given iterations
        for _ in range(self.i):
            d = {}  # dict to store clusters

            # compare
            for i in range(len(x)):
                # calculate distance
                # distance = np.sqrt((x1 - cx)**2 + (y1 - cy)**2)
                di = []  # list to store distances from each centroid
                for j in cl:
                    di.append(np.sqrt(np.sum((x[i] - j) ** 2)))

                # get lowest value's index
                min_di = di.index(min(di))

                # build clusters with indices
                if min_di not in d.keys():
                    d[min_di] = [i]
                else:
                    d[min_di].append(i)

            # calculate mean and improve centroids
            for i in range(self.k):
                sum_x = 0
                sum_y = 0
                n = len(d[i])
                for j in d[i]:
                    a, b = x[j]
                    sum_x += a
                    sum_y += b
                cl[i] = [sum_x / n, sum_y / n]

        # prepare and return clusters
        for a, b in d.items():
            li = [x[z] for z in b]
            d[a] = li
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
a = KMeans(2, 10)
cl = a.fit(X)
print(f"2k: {cl}")

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
b = KMeans(3, 50)
cl = b.fit(X)
print(f"3k-b: {cl}")

# Customer data: [Age, Income in thousands]
X = np.array(
    [
        # Young, low income
        [25, 30],
        [27, 35],
        [28, 32],
        [26, 33],
        [29, 37],
        # Middle-aged, medium income
        [35, 50],
        [38, 55],
        [40, 52],
        [37, 48],
        # Older, high income
        [55, 80],
        [60, 85],
        [58, 82],
        [62, 88],
        [57, 81],
    ]
)
c = KMeans(3, 100)
cl = c.fit(X)
print(f"3k-c: {cl}")
