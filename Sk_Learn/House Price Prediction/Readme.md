# House Price Prediction (Scikit-Learn)

This project is a **beginner-friendly machine learning pipeline** that predicts house prices using **Scikit-Learn**, **Random Forest Regression**, and a clean data-processing workflow.  
It loads housing data, performs preprocessing, trains a model, and saves both the model and pipeline for later inference.

## Features

- **Train/test split** using *StratifiedShuffleSplit* based on income categories  
- **Preprocessing pipeline**  
  - Numerical: median imputation + standard scaling  
  - Categorical: one-hot encoding  
- **Random Forest Regression** for price prediction  
- Saves:
  - `model.pkl` — trained model  
  - `pipeline.pkl` — preprocessing pipeline  
  - `test.csv` — test data  
  - `output.csv` — predictions  
- Automatically switches to *inference mode* when the model already exists

## How It Works

### **1. Training Mode (first run)**  
Triggered when `model.pkl` does **not** exist.

1. Loads `data.csv`  
2. Creates a stratified split using income categories  
3. Saves test data to `test.csv`  
4. Builds preprocessing pipelines for numeric and categorical features  
5. Trains a `RandomForestRegressor`  
6. Saves:
   - `model.pkl`
   - `pipeline.pkl`

### **2. Inference Mode**  
Runs when `model.pkl` **already exists**.

1. Loads saved model and pipeline  
2. Loads `test.csv`  
3. Applies preprocessing  
4. Predicts house prices  
5. Saves results to `output.csv`

### To retrain:
1. Delete **model.pkl** and **pipeline.pkl**
1. Run the script again
## Requirements
The following libraries/modules are required:
1. numpy
1. pandas
1. scikit-learn
1. joblib

To install them, run:
``` bash
pip install numpy pandas scikit-learn joblib
```
in your terminal.

## Conclusion
- This project demonstrates the full ML workflow:
```
load data → preprocess → train → save → infer
```

- You can experiment by swapping out the regressor.
- The pipeline ensures consistent transformations between training and inference.
- This is a very good  project for AI/ML beginners.
