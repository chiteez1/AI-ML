import numpy as np

# loss function
def loss(y_pred: np.ndarray, y_true: np.ndarray):
    return np.mean((y_true - y_pred) ** 2)


# function to calculate gradients:
def gradients(
    x: np.ndarray, y_true: np.ndarray, y_pred: np.ndarray
) -> tuple[np.ndarray, np.floating]:

    # calculate error
    err = y_pred - y_true
    n = len(y_true)

    # calculate gradient
    # for weight
    dw = (2 / n) * (x.T @ err)  # computes gradient for each weight

    # for bias
    db = (2 / n) * np.sum(err)
    return dw, db


# linear regression function
def linear_reg(features: np.ndarray, labels: np.ndarray, lr: float = 0.01, patience: int = 100, epochs: int = 10000) -> tuple:

    # get number of columns
    n_features = features.shape[1] if len(features.shape) > 1 else 1

    # check if array is 1D
    if n_features == 1:
        # reshape function makes it 2d. Adds 1 at features.shape[1]: (5,1)
        features = features.reshape(-1, 1)

    # initalise weight for each column
    w = np.zeros(n_features)

    # default values
    b = 0

    # store lowest loss. Starting value is infinity
    low_l = float("inf")
    wait = 0  # iteration counter

    # start training
    for i in range(epochs):
        # Prediction
        pd = (features @ w) + b

        # Calculate loss
        current_l = loss(pd, labels)

        # print loss after every 1000 iterations for understanding
        if i % 1000 == 0:
            print(current_l)

        # check if current loss is lower than lowest loss
        if current_l < low_l:
            wait = 0
            low_l = current_l

        # if no, increase wait by +1
        else:
            wait += 1

        # stops the loop if loss keeps increasing for given number of iterations
        if wait >= patience:
            break

        # calculate derivatives for weights and bias
        dw, db = gradients(features, labels, pd)

        # update weight and bias
        w -= lr * dw
        b -= lr * db
    print("Lowest loss:", low_l)
    return w, b


# One feature
X = np.array([1, 2, 3, 4, 5])
y = 2 * X + 3
w, b = linear_reg(X, y)
print(f"Weight: {w}\nbias: {b}")

# Two features
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = 2 * X[:, 0] + 3 * X[:, 1] + 1  # y = 2 * x1 + 3 * x2 + 1
w, b = linear_reg(X, y, 0.001, 1000, 50000)
print(f"Weights: {w}")
print(f"Bias: {b}")
