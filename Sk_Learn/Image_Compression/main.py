import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

# load image
img = Image.open("img.jpg")
img = img.resize((256, 256))
arr = np.array(img)
features = arr.reshape(-1, 3)

# train model
k = 16
model = KMeans(n_clusters=k, random_state=42)
labels = model.fit_predict(features)
centr = model.cluster_centers_
new_img = centr[labels]
new_img = new_img.reshape(256, 256, 3)
new_img = new_img.astype(np.uint8)

# Plot
# original
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(arr)
axes[0].axis("off")
axes[0].set_title("Original Image")

# Compressed
axes[1].imshow(new_img)
axes[1].axis("off")
axes[1].set_title("Compressed Image")
plt.show()
