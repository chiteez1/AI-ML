# Decision trees from scratch
import numpy as np

# Task
# complete find_split()
# complete the tree class


def gini(tu) -> float:
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
            print(f"Thr: {thr}")

            # split based on idx
            for k in idx:
                if features[k] <= thr:
                    left_idx.append(k)
                else:
                    right_idx.append(k)

            # allocate left and right groups
            left = (x[left_idx], y[left_idx])
            right = (x[right_idx], y[right_idx])
            print(f"Left: {left}\nRight: {right}")

            # calculate gini
            gi = (
                (gini(left) * (len(left[-1]) / f_ln))
                + (gini(right) * (len(right[-1]) / f_ln))
            ) / 2

            print(f"Gi: {gi}")

            # check if gi is lowest
            if gi < b_gi:
                # store lowest gini and best groups
                b_gi = gi
                b_left = left
                b_right = right
                b_thr = thr
            else:
                return b_left, b_right, b_thr, i


# class to construct Nodes
# class Node:
#     # def __init__(self, li: list[tuple[np.ndarray, np.ndarray], ln: int) -> None:
#     #     print(f"Li inside Node: {li}")
#     #     self._x = li
#     #     self._ln = ln
#     #     self._thr = []
#     #     self._left = None
#     #     self._right = None
#     def __init__(self, x: np.ndarray, y: np.ndarray, ln: int) -> None:
#         print(f"Li inside Node: {x}")
#         self._x = x
#         self._y = y
#         self._ln = ln
#         self._thr = []
#         self._left = None
#         self._right = None

#     # function to construct node
#     def train(self):
#         # store lowest gini and best groups
#         b_gi = float("inf")
#         b_left = None
#         b_right = None

#         # iterate through the cols
#         for i in range(self._ln):
#             print(f"self._x: {self._x[i]}")
#             features, y = self._x[i]
#             f_ln = len(features)
#             for j in range(f_ln - 1):
#                 # construct lists for groups
#                 # left = np.array([])
#                 # right = np.array([])
#                 left = []
#                 right = []

#                 # calculate threshold
#                 j1 = j + 1
#                 thr = (features[j] + features[j1]) / 2

#                 # split
#                 for k in range(f_ln):
#                     # if features[k] <= thr:
#                     #     left = np.append(left, (features[k], y[k]))
#                     # else:
#                     #     right = np.append(right, (features[k], y[k]))
#                     if features[k] <= thr:
#                         left.append((self._x[: self._ln], y[k]))
#                     else:
#                         right.append((self._x[: self._ln], y[k]))

#                 # calculate gini
#                 gi = (
#                     (gini(left) * (len(left) / f_ln))
#                     + (gini(right) * (len(right) / f_ln))
#                 ) / 2
#                 # check if gi is lowest
#                 if gi < b_gi:
#                     b_gi = gi
#                     b_left = left
#                     b_right = right
#                 else:
#                     self._thr.append([thr, i])
#                     return b_left, b_right


#                 # store lowest gini and best groups
class Node:
    def __init__(self, x: np.ndarray, y: np.ndarray, ln: int) -> None:
        self._x = x
        self._y = y
        self._ln = ln
        self._thr = []
        self._left = None
        self._right = None
        self._leaf = False

    # function to construct node
    def train(self):
        # store lowest gini and best groups
        b_thr = None
        b_gi = float("inf")
        b_left = None
        b_right = None

        # iterate through the cols
        for i in range(self._ln):
            features = self._x[:, i]
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
                print(f"Thr: {thr}")

                # split based on idx
                for k in idx:
                    if features[k] <= thr:
                        left_idx.append(k)
                    else:
                        right_idx.append(k)

                # allocate left and right groups
                left = (self._x[left_idx], self._y[left_idx])
                right = (self._x[right_idx], self._y[right_idx])
                print(f"Left: {left}\nRight: {right}")

                # calculate gini
                gi = (
                    (gini(left) * (len(left[-1]) / f_ln))
                    + (gini(right) * (len(right[-1]) / f_ln))
                ) / 2

                print(f"Gi: {gi}")
                # check if gi is lowest
                if gi < b_gi:
                    # store lowest gini and best groups
                    b_gi = gi
                    b_left = left
                    b_right = right
                    b_thr = thr
                else:
                    self._thr.append(b_thr)
                    self._thr.append(i)
                    return b_left, b_right

    # function to predict values
    def predict(self, x: np.ndarray, y: list = []):
        # if self._leaf:
        #     # y = []
        #     # for i in features:
        #     #     if i <= thr:
        #     #         y.append(0)
        #     #     else:
        #     #         y.append(1)
        #     # y = (x[:, n] > thr).astype(int)
        #     print(f"Return: {y}")
        #     return y
        # else:
        #     left = np.array([])
        #     right = np.array([])
        #     left_y = []
        #     right_y = []
        #     features = x[:, n]
        #     for i in range(len(features)):
        #         if features[i] <= thr:
        #             left = np.append(left, x[i], axis=0)
        #             left_y.append(0)
        #         else:
        #             right = np.append(right, x[i], axis=0)
        #             right_y.append(1)
        #     print(f"Returning {left}, {right}")
        #     return left, left_y, right, right_y
        print(f"thr: {self._thr}")
        thr, n = self._thr[0], self._thr[1]
        print(f"Prediction using {n} column")
        print(f"x: {x}")
        left = np.array([])
        right = np.array([])
        left_y = []
        right_y = []
        features = x[:, n]
        for i in range(len(features)):
            if features[i] <= thr:
                left = np.append(left, x[i], axis=0)
                left_y.append(0)
            else:
                right = np.append(right, x[i], axis=0)
                right_y.append(1)
        print(f"Returning {left}, {right}")
        return left, left_y, right, right_y


# class to build tree
class dec_Tree:
    def __init__(self) -> None:
        self._root = None
        pass

    def fit(self, features: np.ndarray, labels: np.ndarray, n_columns: int) -> Node:
        # x = self.sort_arr()
        nd = Node(features, labels, n_columns)
        # self._root = nd

        # base case
        if len(np.unique_values(labels)) <= 1:
            nd._leaf = True
            return nd

        # get values
        (left_x, left_y), (right_x, right_y) = nd.train()
        print("Execute left!")
        nd._left = fit(left_x, left_y, n_columns)
        print("Execute right!")
        nd._left = fit(right_x, right_y, n_columns)
        return nd

    def print_tree(self, nd) -> None:
        if nd._leaf:
            print("-------- Leaf -------")
            print(f"thr: {nd._thr}")
            print(f"x: {nd._x}")
            print(f"y: {nd._y}")
            return
        print("-------- Node ---------")
        print(f"self._thr: {nd._thr}")
        print(f"self._x: {nd._x}")
        print(f"self._y: {nd._y}")

        print("------ Left -------")
        print(f"thr: {nd._left._thr}")
        print(f"x: {nd._left._x}")
        print(f"y: {nd._left._y}")
        print_tree(nd._left)

        print("------ Right -------")
        print(f"thr: {nd._right._thr}")
        print(f"x: {nd._right._x}")
        print(f"y: {nd._right._y}")
        print_tree(nd._right)


# function to construct node
# def node(x: list[tuple], ln: int) -> float | int:
#     # iterate through the cols
#     for i in range(ln):
#         features, y = x[i]
#         f_ln = len(features)
#         for j in range(f_ln - 1):
#             # construct lists for groups
#             left = np.array([])
#             right = np.array([])

#             # calculate threshold
#             j1 = j + 1
#             thr = (features[j] + features[j1]) / 2

#             # split
#             for k in range(f_ln):
#                 if features[k] <= thr:
#                     left = np.append(left, y[k])
#                 else:
#                     right = np.append(right, y[k])
#             gi = (
#                 (gini(left) * (len(left) / f_ln)) + (gini(right) * (len(right) / f_ln))
#             ) / 2
#             if gi == 0.0:
#                 print(f"Gini: {gi}")
#                 return thr
#     return -1


# function to construct tree
# def dec_tree(li: list[tuple[np.ndarray, np.ndarray]], n_columns: int = 1):
#     nd = Node(li, n_columns)
#     if len(li) <= 1:
#         return nd
#     left, right = nd.train()
#     print("Execute Left!")
#     nd._left = dec_tree(left, n_columns)
#     print("Execute Right!")
#     nd._right = dec_tree(right, n_columns)
#     print("Return Node")
#     return nd


# def dec_tree(features: np.ndarray, labels: np.ndarray, n_columns: int = 1) -> Node:
#     nd = Node(features, labels, n_columns)

#     # base case
#     if len(np.unique_values(labels)) <= 1:
#         print(f"Leaf true: {features}, {labels}")
#         nd._leaf = True
#         return nd


#     # get values
#     (left_x, left_y), (right_x, right_y) = nd.train()
#     # print("Dec_Tree:", left_x, left_y, right_x, right_y)
#     print("Execute Left!")
#     nd._left = dec_tree(left_x, left_y, n_columns)
#     print("Execute Right!")
#     nd._right = dec_tree(right_x, right_y, n_columns)
#     print("Return Node")
#     return nd


def dec_tree(features: np.ndarray, labels: np.ndarray, n_columns: int = 1) -> Node:
    nd = Node(features, labels, n_columns)

    # base case
    if len(np.unique_values(labels)) <= 1:
        print(f"Leaf true: {features}, {labels}")
        nd._leaf = True
        return nd

    # get values
    (left_x, left_y), (right_x, right_y) = nd.train()
    # print("Dec_Tree:", left_x, left_y, right_x, right_y)
    print("Execute Left!")
    nd._left = dec_tree(left_x, left_y, n_columns)
    print("Execute Right!")
    nd._right = dec_tree(right_x, right_y, n_columns)
    print("Return Node")
    return nd


# function to predict values using Tree
def predict_tree(node, features: np.ndarray, labels: list = []):
    # check if leaf
    if node._leaf or features.ndim <= 1:
        # return node.predict(features)
        return labels  # return leaf values

    # split features
    # left, right = node.predict(features)
    left_x, left_y, right_x, right_y = node.predict(features)

    # predict
    left = predict_tree(node._left, left_x, left_y)
    right = predict_tree(node._right, right_x, right_y)
    print(f"Return left: {left}, right: {right}")
    return np.append(left, right)


def print_tree(nd) -> None:
    if nd._leaf:
        print("-------- Leaf -------")
        print(f"thr: {nd._thr}")
        print(f"x: {nd._x}")
        print(f"y: {nd._y}")
        return
    print("-------- Node ---------")
    print(f"self._thr: {nd._thr}")
    print(f"self._x: {nd._x}")
    print(f"self._y: {nd._y}")

    print("------ Left -------")
    print(f"thr: {nd._left._thr}")
    print(f"x: {nd._left._x}")
    print(f"y: {nd._left._y}")
    print_tree(nd._left)

    print("------ Right -------")
    print(f"thr: {nd._right._thr}")
    print(f"x: {nd._right._x}")
    print(f"y: {nd._right._y}")
    print_tree(nd._right)


# test gini
# y = np.array([0, 0, 1, 1, 1])
# print(f"Test Gini: {gini(y)}")


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
# sort features
# np.argsort: returns the indices of the array after sorting it. It doesn't sort the array itself.
# li = []
# for i in range(2):
#     idx = np.argsort(X[:, i])
#     f1 = X[idx, i]
#     l1 = y[idx]
#     li.append((f1, l1))
# print(f"Li: {li}")

# build tree
# dec_tree(X, y, 2)
a = dec_tree(X, y, 2)
# print(f"Dec tree left: {a._left}\nDec tree right: {a._right}")
# print("a tree:")
# print_tree(a)

# Test
test = np.array([[5, 20], [19, 42]])
pred = predict_tree(a, test)
print(f"Prediction: {pred}")

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
b = dec_tree(X, y, 2)
# print(f"Dec tree left: {b._left}\nDec tree right: {b._right}")
# print("b tree:")
# print_tree(b)

# Test
test = np.array([[6, 22], [15, 30]])
pred = predict_tree(b, test)
print(f"Prediction: {pred}")
