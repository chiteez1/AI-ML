import numpy as np


# function to calculate loss
def loss(y_pred: np.ndarray, y_true: np.ndarray) -> np.floating:
    return -np.mean((y_true * np.log(y_pred)) + ((1 - y_true) * np.log(1 - y_pred)))


# sigmoid function
def sigmoid(y_pred: np.ndarray) -> np.ndarray:
    classes = 1 / (1 + np.exp(-y_pred))
    return classes


# function to calculate gradients
def gradients(x: np.ndarray, y_pred: np.ndarray, y_true: np.ndarray) -> tuple:
    # calculate error
    err = y_pred - y_true
    n = len(y_true)

    # calculate gradients
    # for weights
    dw = (1 / n) * (x.T @ err)

    # for bias
    db = (1 / n) * np.sum(err)

    return dw, db


def log_reg(
    features: np.ndarray, labels: np.ndarray, lr: float = 0.01, epochs: int = 1000
) -> tuple:
    # check if features array is 2d
    n = features.shape[1] if len(features.shape) > 1 else 1

    # if not, make it 2d
    if n == 1:
        features = features.reshape(-1, 1)

    # allocate starting values
    w = np.zeros(n)
    b = 0.1
    wait = 0
    patience = 100
    best_l = float("inf")

    # trainig loop
    for _ in range(epochs):
        pd = sigmoid((features @ w) + b)
        cur_l = loss(pd, labels)
        print(f"Loss: {cur_l}")

        # check if loss is decreasing
        if cur_l < best_l:
            wait = 0
            best_l = cur_l

        # if not, increase wait by 1
        else:
            wait += 1

        # stop training if loss increases for patience no. of consecutive epochs
        if wait >= patience:
            break

        # calculate gradients
        dw, db = gradients(features, pd, labels)

        # update weights and bias
        w -= lr * dw
        b -= lr * db

    return w, b


# Test model
X = np.array(
    [[1, 2], [2, 3], [3, 3], [2, 1], [3, 2], [6, 6], [7, 7], [8, 6], [7, 5], [6, 7]]
)

y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

w, b = log_reg(X, y, lr=0.001, epochs=100000)
print(f"Weights: {w}")
print(f"Bias: {b}")

# Predict class labels
y = (X @ w) + b
predictions = sigmoid(y)
print(f"Predictions: {predictions}")
print(f"Classes: {(predictions > 0.5).astype(int)}")
