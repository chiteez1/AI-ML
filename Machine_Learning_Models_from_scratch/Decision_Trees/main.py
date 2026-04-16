# Decision trees from scratch
import numpy as np


# Leaf class
class Leaf:
    def __init__(self, val) -> None:
        self._value = val


# Node class
class Node:
    def __init__(self) -> None:
        self._thr = 0.0
        self._nth_col = 0
        self._left = None
        self._right = None
        pass


# class to build tree
class dec_Tree:
    def __init__(self) -> None:
        self._root = None

    # training function
    def fit(
        self, features: np.ndarray, labels: np.ndarray, n_columns: int
    ) -> Node | Leaf:
        # base case: check if leaf
        if len(np.unique(labels)) <= 1:
            lf = Leaf(labels[0])
            return lf

        # construct node
        nd = Node()
        if self._root is None:
            self._root = nd

        # get best split values
        (left_x, left_y), (right_x, right_y), thr, i = find_split(
            features, labels, n_columns
        )

        # set threshold and decision feature no.
        nd._thr = thr
        nd._nth_col = i
        nd._left = self.fit(left_x, left_y, n_columns)
        nd._right = self.fit(right_x, right_y, n_columns)
        return nd

    # function to predict with a single sample
    def pred(self, z, x: np.ndarray) -> int | str:
        # base case: check if leaf node
        if isinstance(z, Leaf):
            return z._value

        # get threshold and decision column value
        thr = z._thr
        n_col = z._nth_col
        feature = x[n_col]

        # compare and pass
        if feature <= thr:
            return self.pred(z._left, x)
        else:
            return self.pred(z._right, x)

    # function to predict values with multiple samples
    def predict_tree(self, features: np.ndarray) -> np.ndarray:
        # start with root node
        z = self._root
        return np.array([self.pred(z, x) for x in features])

    # function to print tree structure
    def print_tree(self, z) -> None:
        if isinstance(z, Leaf):
            print("-------- Leaf -------")
            print(f"Val: {z._value}")
            return
        print("-------- Node ---------")
        print(f"self._thr: {z._thr}")
        print(f"self._nth_col: {z._nth_col}")

        print("------ Left -------")
        self.print_tree(z._left)

        print("------ Right -------")
        self.print_tree(z._right)


def gini(tu: tuple) -> float:
    x = tu[-1]

    # calculate no. of elements
    _, ct = np.unique(x, return_counts=True)

    # calculate total no. of elements
    ct_ln = np.sum(ct)

    # compute probabilities
    prob = ct / ct_ln
    return 1 - np.sum(prob**2)


# function to find best split
def find_split(x: np.ndarray, y: np.ndarray, n_cols: int):
    # store lowest gini and best groups
    b_thr = None
    b_gi = float("inf")
    b_left = None
    b_right = None
    n = 0

    # iterate through the cols
    for i in range(n_cols):
        features = x[:, i]
        f_ln = len(features)

        # sort features and labels
        # np.argsort: returns the indices of the array after sorting it. It doesn't sort the array itself.
        idx = np.argsort(features)
        sort_x = features[idx]

        for j in range(f_ln - 1):
            # construct lists for groups
            left_idx = []
            right_idx = []

            # calculate threshold
            j1 = j + 1
            thr = (sort_x[j] + sort_x[j1]) / 2

            # split based on idx
            for k in idx:
                if features[k] <= thr:
                    left_idx.append(k)
                else:
                    right_idx.append(k)

            # allocate left and right groups
            left = (x[left_idx], y[left_idx])
            right = (x[right_idx], y[right_idx])

            # calculate gini
            gi = (gini(left) * (len(left[-1]) / f_ln)) + (
                gini(right) * (len(right[-1]) / f_ln)
            )

            # check if gi is lowest
            if gi < b_gi:
                # store lowest gini and best groups and n_col
                b_gi = gi
                b_left = left
                b_right = right
                b_thr = thr
                n = i
    return b_left, b_right, b_thr, n


# simple dataset
a_X = np.array(
    [
        [5, 20],  # Cat
        [7, 25],  # Cat
        [6, 22],  # Cat
        [18, 40],  # Dog
        [20, 45],  # Dog
        [19, 42],  # Dog
    ]
)

a_y = np.array([0, 0, 0, 1, 1, 1])  # 0=Cat, 1=Dog

# build tree
a = dec_Tree()
a.fit(a_X, a_y, 2)
a.print_tree(a._root)

# complex dataset
b_X = np.array(
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

b_y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0, 1])
b = dec_Tree()
b.fit(b_X, b_y, 2)
b.print_tree(b._root)

# XOR pattern
c_X = np.array(
    [[0, 0], [0, 1], [1, 0], [1, 1], [0.1, 0.1], [0.1, 0.9], [0.9, 0.1], [0.9, 0.9]]
)

c_y = np.array([0, 1, 1, 0, 0, 1, 1, 0])

c = dec_Tree()
c.fit(c_X, c_y, 2)
c.print_tree(c._root)

# Test
# a tree
a_pred = a.predict_tree(a_X)
accuracy = np.mean([a_pred == a_y])
print(f"Accuracy(a): {accuracy * 100:.1f}%")


# b tree
b_pred = b.predict_tree(b_X)
accuracy = np.mean([b_pred == b_y])
print(f"Accuracy(b): {accuracy * 100:.1f}%")

# c tree
c_pred = c.predict_tree(c_X)
accuracy = np.mean([c_pred == c_y])
print(f"Accuracy(c): {accuracy * 100:.1f}%")
