# Image Compression with K-Means Clustering

A lightweight Python script that compresses images using K-Means clustering. It reduces the number of unique colors in an image to a fixed palette, then displays the original and compressed versions side by side for easy comparison.

## How It Works

The script treats each pixel as a point in 3D color space (R, G, B) and runs K-Means clustering to group similar colors together. Each pixel is then replaced with its cluster's centroid color. It effectively reduces the image to just 16 distinct colors while preserving the overall visual structure.

## Requirements

Install the dependencies with pip:

```bash
pip install numpy pillow scikit-learn matplotlib
```

## Usage

Place your image in the same directory as the script and name it `img.jpg`, then run:

```bash
python compress.py
```

A window will open showing the original and compressed images side by side.

## Configuration

You can tweak the compression by changing the `k` variable near the top of the script:

```python
k = 16  # Number of colors in the compressed image
```

Lower values mean stronger compression and a more stylized look. Higher values preserve more color detail. The image is also resized to 256×256 pixels before processing. You can adjust that in the `img.resize()` call.

## Example Output

| Original | Compressed (k=16) |
|----------|-------------------|
| Full color range | 16-color palette |

## Limitations

- The input file must be named `img.jpg` and placed in the same directory
- The image is resized to 256×256 before processing, so very large images will be downscaled
- K-Means is non-deterministic by nature, though `random_state=42` is set for reproducibility
