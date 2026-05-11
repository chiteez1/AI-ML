import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Train
df = pd.read_csv("Customers_data.csv")
scaler = StandardScaler()
features = scaler.fit_transform(df[["Annual Income (k$)", "Spending Score (1-100)"]])
kmeans = KMeans(n_clusters=5, random_state=42)
labels = kmeans.fit_predict(features)
centroids = kmeans.cluster_centers_

# Visualise
for i in range(5):
    f = features[labels == i]
    plt.scatter(f[:, 0], f[:, 1], label=i)
plt.scatter(centroids[:, 0], centroids[:, 1], marker="X", s=100)
plt.title("Centroids and Clusters")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1 - 100)")
plt.legend()
plt.tight_layout()
plt.savefig("output.png")
