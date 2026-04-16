# Decision Tree Classifier (From Scratch)
A simple and educational implementation of a **Decision Tree classifier using NumPy**, built completely from scratch without any machine learning libraries. This project is designed to help me understand how decision trees work internally — from splitting logic to recursive tree construction.

## Features
- Built from scratch using only NumPy  
- Uses **Gini Impurity** for splitting  
- Recursive tree construction  
- Supports multi-sample prediction  
- Includes tree visualization (console-based)  
- Handles non-linear patterns (e.g., XOR)

## How It Works
The model builds a binary tree by:
1. Iterating through all features  
2. Trying different split thresholds  
3. Calculating **Gini Impurity** for each split  
4. Choosing the split that minimizes impurity  
5. Recursively repeating for child nodes  

### Gini Impurity

```
Gini = 1 - Σ(p_i²)
```

Where `p_i` is the probability of each class in a node.

## Project Structure

```
.
├── main.py
└── README.md
```

## Installation

Make sure you have Python 3 installed, then install NumPy:

```bash
pip install numpy
```

## Usage

### Train the Model

```python
tree = dec_Tree()
tree.fit(features, labels, n_columns)
```

### Make Predictions

```python
predictions = tree.predict_tree(features)
```

### Print Tree Structure

```python
tree.print_tree(tree._root)
```

## Example Datasets

The script includes three datasets:

### 1. Simple Dataset
Linearly separable (Cats vs Dogs)
``` python
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
```

### 2. Complex Dataset
- Includes edge cases and overlapping features
``` python
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
```

### 3. XOR Pattern
- Classic non-linear problem
``` python
X = np.array(
    [[0, 0], [0, 1], [1, 0], [1, 1], [0.1, 0.1], [0.1, 0.9], [0.9, 0.1], [0.9, 0.9]]
)

y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
```
## Results
```
Accuracy(a): 100.0%
Accuracy(b): 100.0%
Accuracy(c): 100.0%
```

## Scope & Limitations

This implementation is intentionally designed for **learning and clarity**, not production use. The limitations of this project are as follows:
1. Uses brute-force split search for transparency
2. Does not include pruning (kept minimal for understanding tree growth)
3. No handling of missing values
4. Performance is not optimized for large datasets

## What This Project Covers

This project focuses on understanding the core mechanics of decision trees:
1. Recursive tree construction  
2. Gini impurity and split evaluation  
3. Feature-based threshold splitting
4. Handling non-linear patterns (e.g., XOR)  
The goal is clarity and learning, rather than building a production-ready model.

## License

This project is open-source and free to use for educational purposes.

## Acknowledgements

Inspired by how decision trees are implemented in libraries like scikit-learn, but simplified for learning.

## Conclusion

This implementation focuses on understanding how decision trees work under the hood, from split selection to recursive structure building. It prioritizes clarity and learning over performance or production use.
