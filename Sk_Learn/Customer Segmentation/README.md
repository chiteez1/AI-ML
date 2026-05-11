# Customer Segmentation with K-Means Clustering

A lightweight Python script that groups customers into distinct segments based on their annual income and spending behaviour, then produces a clear cluster visualisation.


## What It Does

The script reads a customer dataset, standardises the relevant features, and runs K-Means clustering to identify five natural customer groups. It then plots each cluster alongside its centroid and saves the result as a PNG image — ready for presentations or further analysis.


## Requirements

- Python 3.7+
- pandas
- scikit-learn
- matplotlib

#### Install dependencies with:

```bash
pip install pandas scikit-learn matplotlib
```


## Usage

1. Place your `Customers_data.csv` file in the same directory as the script.
2. Run the script:

```bash
python customer_segmentation.py
```

3. The output chart will be saved as `output.png` in the same directory.


## Input Data

The script expects a CSV file named `Customers_data.csv` with at least the following two columns:

| Column | Description |
|---|---|
| `Annual Income (k$)` | Customer's annual income in thousands of dollars |
| `Spending Score (1-100)` | A score assigned based on customer spending behaviour |


## Output

A scatter plot (`output.png`) showing:

- **Five colour-coded clusters**, each representing a distinct customer segment
- **Centroid markers (✕)** indicating the centre of each cluster

This chart gives an at-a-glance view of how customers distribute across income and spending dimensions.


## How It Works

1. **Load** — the dataset is read from `Customers_data.csv` using pandas.
2. **Scale** — annual income and spending score are standardised with `StandardScaler` so neither feature dominates the distance calculation.
3. **Cluster** — K-Means is fit with `k=5` clusters and a fixed random seed (`random_state=42`) for reproducibility.
4. **Visualise** — each cluster is plotted in a distinct colour, with centroid positions marked, and the figure is saved to disk.


## Configuration

To experiment with a different number of clusters, update the `n_clusters` parameter:

```python
kmeans = KMeans(n_clusters=5, random_state=42)  # change 5 to your desired k
```


## License

This project is released under the MIT License.
