# KMeans Clustering — Pure NumPy Implementation

A lightweight, from-scratch implementation of the K-Means clustering algorithm using only NumPy. No machine learning frameworks required.

---

## Overview

This project implements K-Means clustering entirely from the ground up, without relying on libraries like scikit-learn. It's a clean, readable implementation that's great for understanding how the algorithm works under the hood — or for use in environments where heavier ML dependencies aren't practical.

The algorithm groups unlabelled data points into `k` clusters by iteratively assigning each point to its nearest centroid and recalculating centroids until convergence (or until a maximum number of iterations is reached).

---

## How It Works

1. **Initialization** — `k` centroids are randomly selected from the dataset.
2. **Assignment** — Each data point is assigned to the nearest centroid using Euclidean distance.
3. **Update** — Each centroid is recalculated as the mean of all points assigned to it.
4. **Repeat** — Steps 2 and 3 repeat for a fixed number of iterations (`max_i`).

---

## Requirements

- Python 3.10+
- NumPy

Install the dependency with:

```bash
pip install numpy
```

---

## Example Usage

```python
import numpy as np
from kmeans import KMeans

X = np.array([
    [1, 2], [1.5, 1.8], [2, 1],
    [8, 8], [8.5, 8.2], [9, 8],
])

model = KMeans(k=2, max_i=10)
clusters = model.fit(X)

print(clusters)
```

### Parameters

| Parameter | Type  | Description                                      |
|-----------|-------|--------------------------------------------------|
| `k`       | `int` | Number of clusters to form                       |
| `max_i`   | `int` | Maximum number of iterations to run              |

### Return Value

`fit()` returns a dictionary where each key is a cluster index (0 to k-1), and each value is a list of NumPy arrays representing the data points assigned to that cluster.

```python
{
    0: [array([1. , 2. ]), array([1.5, 1.8]), ...],
    1: [array([8. , 8. ]), array([8.5, 8.2]), ...],
}
```

---

## Built-in Examples

The script includes three demonstration runs:

### **Two geometric clusters**
Nine 2D points that naturally separate into two groups. Run with `k=2, max_i=10`.
``` python
# 2 clear clusters in 2D
X = np.array(
    [
        [1, 2],
        [1.5, 1.8],
        [2, 1],
        [1.2, 2.5],
        [8, 8],
        [8.5, 8.2],
        [9, 8],
        [8, 9],
        [7.5, 8.5],
    ]
)
a = KMeans(2, 10)
cl = a.fit(X)
print(f"2k: {cl}")
```
---

### **Three geometric clusters**
Twelve points spread across three distinct regions of the 2D plane. Run with `k=3, max_i=50`.
``` python
# 3 clusters in 2D
X = np.array(
    [
        # Cluster 1 (bottom-left)
        [1, 1],
        [1.5, 2],
        [2, 1.5],
        [1.2, 1.8],
        # Cluster 2 (top-middle)
        [5, 8],
        [5.5, 8.5],
        [6, 8],
        [5.2, 7.8],
        # Cluster 3 (bottom-right)
        [9, 2],
        [9.5, 2.5],
        [10, 2],
        [9.2, 1.8],
    ]
)
b = KMeans(3, 50)
cl = b.fit(X)
print(f"3k-b: {cl}")
```
---
### **Customer segmentation**
Fourteen data points representing customer age and annual income. The algorithm segments them into three groups: young/low-income, middle-aged/medium-income, and older/high-income. Run with `k=3, max_i=100`.
``` python
# Customer data: [Age, Income in thousands]
X = np.array(
    [
        # Young, low income
        [25, 30],
        [27, 35],
        [28, 32],
        [26, 33],
        [29, 37],
        # Middle-aged, medium income
        [35, 50],
        [38, 55],
        [40, 52],
        [37, 48],
        # Older, high income
        [55, 80],
        [60, 85],
        [58, 82],
        [62, 88],
        [57, 81],
    ]
)
c = KMeans(3, 100)
cl = c.fit(X)
print(f"3k-c: {cl}")
```


## Limitations
This implementation is intentionally designed for learning and clarity, not production use. The limitations of this project are as follows:
- Centroids are initialised randomly, so results can vary between runs (the seed is fixed to `42` in the examples for reproducibility).
- The algorithm always runs for the full `max_i` iterations — there is no early stopping on convergence.
- Currently supports 2D data points only.

---

## License

This project is open for personal and educational use. Feel free to adapt it as needed.
