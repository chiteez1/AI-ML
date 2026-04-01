# Decision trees from scratch
import numpy as np

# function to calculate gini
def gini(x: np.ndarray) -> float:
    # calculate no. of elements
    _, ct = np.unique(x, return_counts=True)

    # calculate total no. of elements
    ct_ln = np.sum(ct)

    # compute probabilities
    prob = ct / ct_ln
    return 1 - np.sum(prob**2)


# class to construct Nodes
class Node:
    def __init__(self, li: list[tuple[np.ndarray, np.ndarray]], ln: int) -> None:
        self._x = li
        self._ln = ln
        self._thr = None

    # function to construct node
    def train(self):
        # store lowest gini and best groups
        b_gi = float("inf")
        b_left = None
        b_right = None

        # iterate through the cols
        for i in range(self._ln):
            features, y = self._x[i]
            f_ln = len(features)
            for j in range(f_ln - 1):
                # construct lists for groups
                left = np.array([])
                right = np.array([])

                # calculate threshold
                j1 = j + 1
                thr = (features[j] + features[j1]) / 2

                # split
                for k in range(f_ln):
                    if features[k] <= thr:
                        left = np.append(left, y[k])
                    else:
                        right = np.append(right, y[k])

                # calculate gini
                gi = (
                    (gini(left) * (len(left) / f_ln))
                    + (gini(right) * (len(right) / f_ln))
                ) / 2
                # check if gi is lowest
                if b_gi < gi:
                    self._thr = thr
                    return b_left, b_right

                # store lowest gini and best groups
                b_gi = gi
                b_left = left
                b_right = right


# class to build tree
class dec_Tree:
    def __init__(
        self, features: np.ndarray, labels: np.ndarray, n_columns: int
    ) -> None:
        self._x = features
        self._y = labels
        self._ln = n_columns

    def sort_arr(self) -> list[tuple[np.ndarray, np.ndarray]]:
        # sort features
        # np.argsort: returns the indices of the array after sorting it. It doesn't sort the array itself.
        li = []
        for i in range(self._ln):
            idx = np.argsort(self._x[:, i])
            f1 = self._x[idx, i]
            l1 = self._y[idx]
            li.append((f1, l1))
        print(f"Li: {li}")
        return li

    def fit(self):
        x = self.sort_arr()
        n = Node(x, self._ln)
        left, right =


# function to construct node
def node(x: list[tuple], ln: int) -> float | int:
    # iterate through the cols
    for i in range(ln):
        features, y = x[i]
        f_ln = len(features)
        for j in range(f_ln - 1):
            # construct lists for groups
            left = np.array([])
            right = np.array([])

            # calculate threshold
            j1 = j + 1
            thr = (features[j] + features[j1]) / 2

            # split
            for k in range(f_ln):
                if features[k] <= thr:
                    left = np.append(left, y[k])
                else:
                    right = np.append(right, y[k])
            gi = (
                (gini(left) * (len(left) / f_ln)) + (gini(right) * (len(right) / f_ln))
            ) / 2
            if gi == 0.0:
                print(f"Gini: {gi}")
                return thr
    return -1


# function to construct tree
# def dec_tree(features: np.ndarray, labels: np.ndarray, n_columns: int = 1):
#     nd = Node(li, n_columns)
#     left, right = nd.train()
#     print(f"Left: {left}\nRight: {right}")


# test gini
y = np.array([0, 0, 1, 1, 1])
print(f"Test Gini: {gini(y)}")


# simple dataset
X = np.array(
    [
        [5, 20],  # Cat
        [7, 25],  # Cat
        [6, 22],  # Cat
        [18, 40],  # Dog
        [20, 45],  # Dog
        [19, 42],  # Dog
    ]
)

y = np.array([0, 0, 0, 1, 1, 1])  # 0=Cat, 1=Dog

# build tree
# dec_tree(X, y, 2)

# complex dataset
X = np.array(
    [
        [5, 20],  # Cat
        [7, 25],  # Cat
        [6, 22],  # Cat
        [12, 35],  # Cat (tall)
        [18, 40],  # Dog
        [20, 45],  # Dog
        [19, 42],  # Dog
        [8, 38],  # Dog (short)
        [15, 30],  # Cat (fat)
        [21, 48],  # Dog
    ]
)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0, 1])
