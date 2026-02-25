import numpy as np


# Perceptron from Scratch.
class Neuron:
    def __init__(self, w_n: int, sig: bool = False) -> None:
        self._w = np.zeros(w_n)
        self._b = 0
        self._sig = sig

    # loss function
    def loss(self, y_pred: np.ndarray, y_true: np.ndarray):
        if self._sig:
            # Binary cross-entropy for sigmoid
            epsilon = 1e-15
            return -np.mean(
                (y_true * np.log(y_pred + epsilon))
                + ((1 - y_true) * np.log(1 - y_pred + epsilon))
            )
        else:
            # MSE for linear/ReLU
            return np.mean((y_pred - y_true) ** 2)

    # sigmoid function
    def sigmoid(self, y_pred: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-y_pred))

    # reLU function: applies ReLU for each sample
    def ReLU(self, y_pred) -> np.ndarray:
        return np.maximum(0, y_pred)

    # function to calculate gradients
    def gradients(self, x: np.ndarray, y_pred: np.ndarray, y_true: np.ndarray) -> tuple:
        # calculate the length of array
        err = y_pred - y_true
        n = len(y_true)

        # check if it uses sigmoid function
        if self._sig:
            # calculate gradients with sigmoid loss
            # for weights
            dw = (1 / n) * (x.T @ err)

            # for bias
            db = (1 / n) * np.sum(err)
        else:
            # calculate gradients with normal loss
            # for weight
            dw = (2 / n) * (x.T @ err)

            # for bias
            db = (2 / n) * np.sum(err)
        return dw, db

    # function to update weights
    def update(self, dw: np.ndarray, db: np.floating, lr: float) -> None:
        self._w -= lr * dw
        self._b -= lr * db

    # function to predict values
    def predict(self, features: np.ndarray) -> np.ndarray:
        pd = (features @ self._w) + self._b
        if self._sig:
            return self.sigmoid(pd)
        else:
            return self.ReLU(pd)

    # function to train neuron
    def train(
        self,
        features: np.ndarray,
        labels: np.ndarray,
        epochs: int = 1000,
        lr: float = 0.01,
        patience: int = 100,
    ) -> None:
        wait = 0
        best_l = float("inf")
        for i in range(epochs):
            pd = self.predict(features)
            current_l = self.loss(pd, labels)

            # print loss after every 1000 iterations
            if i % 1000 == 0:
                print(f"Loss: {current_l}")

            # check if loss is decreasing
            if current_l < best_l:
                wait = 0
                best_l = current_l
            else:
                wait += 1

            # if loss keeps increasing for {patient} no. of iterations, break the loop
            if wait >= patience:
                break

            # calculate gradients
            dw, db = self.gradients(features, pd, labels)

            # update weights and bias
            self.update(dw, db, lr)
        print(f"Lowest loss: {best_l}")


# Linearly separable data
X = np.array(
    [[1, 2], [2, 3], [3, 3], [2, 1], [3, 2], [6, 6], [7, 7], [8, 6], [7, 5], [6, 7]]
)
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# train neuron
nr = Neuron(2, True)
nr.train(X, y, epochs=10000)

# predict using neuron
predictions = nr.predict(X)
print(f"Predictions:")
print(f"{(predictions > 0.5).astype(int)}")
print(f"True labels: {y}")
