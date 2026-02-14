import pandas as pd
import numpy as np
import joblib
import time
import os
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

if not os.path.exists('model.pkl'):
    df = pd.read_csv("SWIGGY_minute.csv")
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date')
    df = df.sort_index()
    df = df.asfreq('1min')
    df = df.ffill(limit=2)
    df.dropna(inplace=True)

    # Create windows
    grp = df.groupby(df.index.date)
    features = []
    labels = []
    for _, j in grp:
        arr = j['close'].copy()
        a = 0
        while a+3 < len(arr):
            b = a+1
            c = a+2
            d = a+3
            features.append([arr[a], arr[b], arr[c]])
            labels.append(arr[d])
            a += 1
    features = np.array(features)
    labels = np.array(labels)

    # Split data
    sp_len = int(0.8 * len(features))
    joblib.dump((features[sp_len:], labels[sp_len:]), 'test.pkl')
    features = features[:sp_len]
    labels = labels[:sp_len]

    # Scaling
    pipeline = Pipeline([
        ('scale', StandardScaler()),
    ])

    features = pipeline.fit_transform(features)
    joblib.dump(pipeline, 'pipeline.pkl')

    # Training
    model = LinearRegression()
    model.fit(features, labels)
    joblib.dump(model, 'model.pkl')

else:
    pipeline = joblib.load('pipeline.pkl')
    model = joblib.load('model.pkl')
    features, labels = joblib.load('test.pkl')

    # Scale features
    features = pipeline.transform(features)

    # Live Simulation
    for i in range(len(labels)):
        predict = model.predict([features[i]])[0]
        actual = labels[i]
        print(f"Prediction: {round(predict, 2)}\nActual price: {actual}")
        time.sleep(3)
        print("\n")
