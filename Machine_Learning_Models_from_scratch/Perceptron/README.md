# Perceptron from Scratch
A single-neuron neural network built entirely with NumPy — no PyTorch, no TensorFlow, no shortcuts. This project is my hands-on deep dive into the math and mechanics that underpin modern machine learning.


## Why I Built This
Most ML courses hand you a `model.fit()` and call it a day. I wanted to actually understand what's happening underneath — how gradients flow, why loss functions differ between tasks, and what early stopping is really doing. So I built it myself.


## What It Does

The `Neuron` class is a fully functional single-layer perceptron that supports:

- **Binary classification** via sigmoid activation + binary cross-entropy loss
- **Regression** via ReLU activation + mean squared error loss
- **Gradient descent** with manually derived weight and bias updates
- **Early stopping** with a configurable patience parameter to prevent wasted compute

No ML frameworks. Just NumPy and math.


## How It Works

```
Input Features → Linear Combination (Xw + b) → Activation → Prediction → Loss → Gradients → Update Weights
```

The two supported modes:

| Mode | Activation | Loss Function | Use Case |
|------|-----------|---------------|----------|
| Classification (`sig=True`) | Sigmoid | Binary Cross-Entropy | binary labels |
| Regression (`sig=False`) | ReLU | Mean Squared Error | Inside a network |


## Quick Start

**Requirements:** Python 3.x, NumPy

```bash
pip install numpy
python neuron.py
```

**Example output:**
```
Loss: 0.6931
Loss: 0.1042
Loss: 0.0314
Lowest loss: 0.0187
Predictions: [0 0 0 0 0 1 1 1 1 1]
True labels:  [0 0 0 0 0 1 1 1 1 1]
```


## Usage

```python
from neuron import Neuron
import numpy as np

# Create a neuron for binary classification
model = Neuron(w_n=2, sig=True)

# Train on your data
model.train(X, y, epochs=10000, lr=0.01, patience=100)

# Predict
predictions = model.predict(X)
binary_preds = (predictions > 0.5).astype(int)
```

**Parameters:**

| Parameter | Description | Default |
|-----------|-------------|---------|
| `w_n` | Number of weights | required |
| `sig` | Use sigmoid (classification) vs ReLU (regression) | `False` |
| `epochs` | Max training iterations | `1000` |
| `lr` | Learning rate | `0.01` |
| `patience` | Early stopping patience | `100` |


## Project Structure

```
├── neuron.py       # Neuron class + example usage
└── README.md
```


## Concepts Demonstrated

- Forward pass and linear algebra with NumPy
- Sigmoid and ReLU activation functions
- Binary cross-entropy and MSE loss derivation
- Analytical gradient computation (no autograd)
- Gradient descent weight updates
- Early stopping to prevent overfitting

## About

Built as part of my effort to strengthen ML fundamentals from first principles. If you're doing the same, feel free to use this as a reference or reach out.
