# Linear Regression from Scratch

A from-scratch implementation of Linear Regression using only **NumPy**.

This project demonstrates a strong understanding of:
- Calculus (gradient computation)
- Linear Algebra (vectorized operations)
- Optimization (Gradient Descent)
- Machine Learning fundamentals (loss minimization & early stopping)

**No ML libraries (like scikit-learn) were used.**

---

## Key Features

- Vectorized implementation using **NumPy**
- Supports single and multiple features
- Manual gradient computation
- Gradient Descent optimization
- Early stopping (patience-based)
- Configurable learning rate and epochs

---

## How It Works

The model minimizes Mean Squared Error (MSE):

L = (1/n) * Σ (y_true - y_pred)^2

Gradients:

dw = (2/n) * Xᵀ (y_pred - y_true)  
db = (2/n) * Σ (y_pred - y_true)

Parameters are updated using Gradient Descent:

w = w - lr * dw  
b = b - lr * db  

---

## Example Usage

### Single Feature

```python
X = np.array([1, 2, 3, 4, 5])
y = 2 * X + 3

w, b = linear_reg(X, y)
print(w, b)
```

#### Expected output
```
w ≈ 2
b ≈ 3
```

### Multiple features
```python
X = np.array([[1, 2],
              [2, 3],
              [3, 4],
              [4, 5],
              [5, 6]])

y = 2 * X[:, 0] + 3 * X[:, 1] + 1

w, b = linear_reg(X, y, lr=0.001, patience=1000, epochs=50000)
print(w, b)
```

#### Expected output
```
w ≈ [2, 3]
b ≈ 1
```

## Why this project
**Understanding ML libraries is good.
Implementing them from scratch is better.**
This project strengthened my mathematical foundation for AI/ML by connecting theory to practical implementation.


