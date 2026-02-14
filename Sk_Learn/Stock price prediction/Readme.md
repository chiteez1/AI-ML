# Stock Price Prediction Using Linear Regression (Sklearn Practice)

## Project Overview
This project is a **simple machine learning practice project** created to learn and understand how to use **scikit-learn** for time-series style prediction.

The model predicts the **next minute's stock price** based on the **previous three minutes' closing prices**, using **Linear Regression**.

> **Goal:** Practice data preprocessing, feature engineering, scaling, model training, saving/loading models, and live prediction simulation using sklearn.


## What This Project Does
- Loads minute-level stock price data (`SWIGGY_minute.csv`)
- Handles missing timestamps and missing values
- Creates sliding window features (last 3 prices → next price)
- Trains a **Linear Regression** model
- Saves the trained model and preprocessing pipeline
- Simulates **live predictions** on test data


## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib


## How It Works

### Data Preprocessing
- Converts `date` column to datetime
- Sets datetime as index
- Resamples data to **1-minute frequency**
- Forward fills missing values (limit = 2)
- Drops remaining NaNs


### Feature Engineering
For each trading day:
- Uses **3 consecutive closing prices** as input features
- Predicts the **4th closing price**

Example:\
Input → [price_t, price_t+1, price_t+2]
Output → price_t+3


### Train/Test Split
- 80% data → Training
- 20% data → Testing
- Test data is saved using `joblib`

### Scaling
- Uses `StandardScaler`
- Scaling pipeline is saved for reuse


### Model Training
- Algorithm: **Linear Regression**
- Trained on scaled features
- Model saved as `model.pkl`

### Live Prediction Simulation
- Loads saved model and pipeline
- Predicts prices one by one
- Prints prediction vs actual price
- Adds a 3-second delay to simulate live data

## How to Run the Project

### 1. Install Dependencies
```bash
pip install pandas numpy scikit-learn joblib
```

### 2. Run the Script
``` bash
python main.py
```

- If model.pkl does not exist → model will be trained.
- If model.pkl exists → live prediction simulation will start.

### Example Output
Prediction: 385.42\
Actual price: 387.1

## About Me

I am a beginner in AI/ML, and this project was built as hands-on practice to learn scikit-learn and basic machine learning concepts.

## Disclaimer

This project is for learning purposes only and should not be used for real financial or trading decisions.
