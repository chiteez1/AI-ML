# Logistic Regression from Scratch

A bare-bones implementation of binary logistic regression using only NumPy. No sklearn, no shortcuts — just the math.


## Why I built this

I wanted to really understand what's happening under the hood when you call `.fit()` on a classifier. So I sat down and implemented the whole thing myself — forward pass, binary cross-entropy loss, gradient descent, the works. It's a simple script, but writing it forced me to think carefully why logistic regression converges the way it does.


## How it works

The model learns a decision boundary by minimizing **binary cross-entropy loss** via **gradient descent**.

---

**Forward pass**

Raw scores are computed as a linear combination of features and weights, then passed through the sigmoid function to squash them into a probability between 0 and 1.

---

**Loss**

Binary cross-entropy is used to measure how far the predicted probabilities are from the true labels.

---

**Backward pass**

Gradients of the loss with respect to the weights and bias are computed analytically and used to update the parameters each epoch.

---

**Early stopping (patience)**

The training loop tracks the best loss seen so far. If loss stops improving for `patience` consecutive epochs, the model can be stopped early to avoid wasted computation.


## Project structure

```
.
└── log_reg.py       # Everything lives here — loss, sigmoid, gradients, and training loop
```


## Requirements

```
numpy
```

Install with:

```bash
pip install numpy
```


## Usage

```python
import numpy as np
from log_reg import log_reg, sigmoid

X = np.array([[1, 2], [2, 3], [6, 6], [7, 7]])
y = np.array([0, 0, 1, 1])

w, b = log_reg(X, y, lr=0.001, epochs=100000)

predictions = sigmoid((X @ w) + b)
classes = (predictions > 0.5).astype(int)
print(classes)
```

**Key parameters**

| Parameter | Default | Description |
|-----------|---------|-------------|
| `lr` | `0.01` | Learning rate |
| `epochs` | `1000` | Max training iterations |


## Sample output

On the built-in toy dataset (two clearly separable clusters), the model converges cleanly and classifies all 10 points correctly.

```
Weights: [1.243 1.187]
Bias: -10.421
Classes: [0 0 0 0 0 1 1 1 1 1]
```


## What I learned

- How the sigmoid function transforms raw scores into probabilities and why it's a natural fit for binary classification
- Deriving the gradients of cross-entropy loss from scratch made backpropagation much less of a black box
- The importance of the learning rate — too high and the loss oscillates, too low and convergence is painfully slow


## Limitations

This is a learning project, not production code. A few things it doesn't handle:

- Multi-class classification
- Regularization (L1/L2)
- Feature scaling / normalization
- Mini-batch or stochastic gradient descent
