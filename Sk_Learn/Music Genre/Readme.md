# Music Genre Classification (GTZAN Dataset)

This project implements a **music genre classification system** using the **GTZAN dataset**. It extracts audio features from `.wav` files using **Librosa**, trains a **Support Vector Machine (SVM)** classifier with **scikit-learn**, and evaluates its performance on a held-out test set.


## Overview

The model classifies music into one of the following 10 genres:

- Blues  
- Classical  
- Country  
- Disco  
- Hip-hop  
- Jazz  
- Metal  
- Pop  
- Reggae  
- Rock  

The workflow includes:
1. Audio feature extraction
2. Dataset preparation and stratified splitting
3. Feature scaling
4. Model training
5. Model persistence and inference

## Features Extracted

For each audio file, the following features are computed and averaged over time:

- **MFCCs** (20)
- **Chroma features** (12)
- **Spectral Contrast** (7)
- **Tonnetz** (6)
- **Zero Crossing Rate**
- **Spectral Centroid**
- **Spectral Bandwidth**

This results in a total of **48 numerical features per track**.

## Tech Stack

- Python
- Librosa
- NumPy
- Pandas
- scikit-learn
- Joblib

## How It Works

### Training Phase
If `model.pkl` does **not** exist:
- Audio features are extracted from all files
- Data is consolidated into a DataFrame
- A **stratified train-test split** (80/20) is performed
- Features are scaled using `StandardScaler`
- An **SVM classifier** is trained
- The trained model and scaler pipeline are saved

Generated files:
- `train1.csv`
- `test1.csv`
- `pipeline.pkl`
- `model.pkl`


### Inference Phase
If `model.pkl` **exists**:
- The saved model and pipeline are loaded
- The test dataset is transformed and classified
- Predictions are generated
- Classification accuracy is printed


## Running the Project

1. Install dependencies:
```bash
pip install numpy pandas librosa scikit-learn joblib
```
2. Ensure the GTZAN dataset is placed correctly.
3. Run the script:
``` bash
python main.py
```

## Evaluation
- Metric used: Accuracy
- Evaluation is performed on a stratified test set to preserve genre distribution.

## Saved Models
1. model.pkl → Trained SVM classifier.
1. pipeline.pkl → Feature scaling pipeline.

These allow fast inference without retraining.

## License
This project is intended for educational and research purposes.

## Conclusion
This project demonstrates the application of **scikit-learn** to build an end-to-end **music genre classification system**. It showcases skills in audio feature extraction using **Librosa**, data preprocessing, model training with **SVMs**, and performance evaluation on a real-world dataset.

The project highlights my ability to design reproducible machine learning pipelines and apply theoretical concepts to practical AI/ML problems.

