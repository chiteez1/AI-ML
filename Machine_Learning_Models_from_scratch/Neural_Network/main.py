import numpy as np

np.random.seed(42)


# loss function (updated)
def loss(y_pred: np.ndarray, y_true: np.ndarray) -> np.floating:
    # Binary cross-entropy for sigmoid
    epsilon = 1e-15
    return -np.mean(
        (y_true * np.log(y_pred + epsilon))
        + ((1 - y_true) * np.log(1 - y_pred + epsilon))
    )


# Perceptron from Scratch (Updated)
class Neuron:
    def __init__(self, w_n: int, sig: bool = False) -> None:
        # set default values
        self._w = np.random.randn(w_n) * 0.1
        self._b = 0.0

        # store True / False whether it uses sigmoid function
        self._sig = sig

        # initialise var to store relu derivative
        if not sig:
            self._relu_dr = None

    # sigmoid function
    def sigmoid(self, y_pred: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-y_pred))

    # reLU function: applies ReLU for each sample and stores ReLU derivative
    def ReLU(self, y_pred) -> np.ndarray:
        self._relu_dr = (y_pred > 0).astype(float)
        return np.maximum(0, y_pred)

    # function to calculate gradients
    def gradients(self, x: np.ndarray, err: np.ndarray, n: int) -> tuple:
        # check if it uses ReLU
        if not self._sig:
            # multiply error by relu derivative
            err = err * self._relu_dr

        # for weights
        dw = (1 / n) * (x.T @ err)

        # for bias
        db = (1 / n) * np.sum(err)
        return dw, db

    # function to update weights and bias
    def update(self, dw: np.ndarray, db: np.floating, lr: float) -> None:
        self._w -= lr * dw
        self._b -= lr * db

    # function to predict values
    def predict(self, features: np.ndarray) -> np.ndarray:
        # check if features are 1d
        if features.ndim == 1:
            # convert to 2d
            features = features.reshape(-1, 1)

        # predict
        pd = (features @ self._w) + self._b

        # apply activation function
        s = self.sigmoid(pd) if self._sig else self.ReLU(pd)
        return s


# class to define a network
class NeuralNetwork:
    def __init__(self, hidden_n: int) -> None:
        # initialize hidden layer
        self._hiddenLayer = []
        for _ in range(hidden_n):
            self._hiddenLayer.append(Neuron(2))

        # initialize output layer
        self._outputLayer = Neuron(hidden_n, True)

        # intialize var to store hidden_layer output
        self._hidden_pred = np.array([])

    # function to make prediction
    def predict_net(self, features: np.ndarray) -> np.ndarray:
        pred = []
        # forward pass to hidden layer
        for i in self._hiddenLayer:
            pred_n = i.predict(features)
            pred.append(pred_n)

        # make prediction
        pred = np.column_stack(pred)
        self._hidden_pred = pred
        pred = self._outputLayer.predict(pred)
        return pred

    # function for back propagation
    def back_prop(
        self, features: np.ndarray, y_pred: np.ndarray, y_true: np.ndarray, lr: float
    ) -> None:

        # calculate error
        err = y_pred - y_true

        # update the output layer
        dw, db = self._outputLayer.gradients(
            self._hidden_pred, err, len(self._hidden_pred)
        )
        self._outputLayer.update(dw, db, lr)

        # calculate the error for hidden layer:
        err_prop = err.reshape(-1, 1) @ self._outputLayer._w.reshape(1, -1)

        # update the hidden layer
        for i in range(len(self._hiddenLayer)):
            dw, db = self._hiddenLayer[i].gradients(
                features, err_prop[:, i], len(features)
            )
            self._hiddenLayer[i].update(dw, db, lr)

    # function to train
    def train(
        self,
        features: np.ndarray,
        labels: np.ndarray,
        epochs: int,
        patience: int,
        lr: float,
    ):
        best_loss = float("inf")
        wait = 0

        for _ in range(epochs):
            pd = self.predict_net(features)
            curr_loss = loss(pd, labels)
            self.back_prop(features, pd, labels, lr)

            # check if loss is decreasing
            if curr_loss < best_loss:
                wait = 0
                best_loss = curr_loss
            else:
                # increase wait counter
                wait += 1
                print("Loss is increasing")

            # break if loss is increasing after patience number of iterations
            if wait >= patience:
                break


# training dataset
X_train = np.array(
    [
        [0.1, 0.6],
        [0.15, 0.71],
        [0.08, 0.9],
        [0.25, 0.5],
        [0.24, 0.1],
        [0.3, 0.2],
    ]
)
y_train = np.array([0, 0, 0, 1, 1, 1])

# testing dataset
X_test = np.array(
    [
        [0.16, 0.85],
        [0.2, 0.3],
    ]
)
y_test = np.array([0, 1])

# train the network
nn = NeuralNetwork(2)
nn.train(X_train, y_train, 100000, 100, 0.01)

# inference the network
prediction = nn.predict_net(X_test)
print(f"Predictions: {prediction}")
