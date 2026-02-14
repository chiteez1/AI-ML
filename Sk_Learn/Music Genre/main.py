# Code for music_genre classification
import os
import kagglehub
import pandas as pd
import librosa as lb
import numpy as np
import joblib
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


if not os.path.exists('./model.pkl'):
    # Downloading data:
    path = kagglehub.dataset_download(
        "andradaolteanu/gtzan-dataset-music-genre-classification")
    print("Path to dataset files:", path)

    # You need to manually paste the data files in the same directory as this file.

    # Extract data:
    genres = ['blues', 'classical', 'country', 'disco',
              'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
    data = []
    for i in genres:
        for j in range(100):
            if j < 10:
                path = f'./Data/genres_original/{i}/{i}.0000{j}.wav'
            else:
                path = f'./Data/genres_original/{i}/{i}.000{j}.wav'

            try:
                y, sr = lb.load(path, sr=22050)

                # MFCC
                mfcc = lb.feature.mfcc(y=y, sr=sr, n_mfcc=20)
                mfcc = np.mean(mfcc, axis=1)

                # Chroma
                chroma = lb.feature.chroma_stft(y=y, sr=sr)
                chroma = np.mean(chroma, axis=1)

                # Spectral contrast
                spr = lb.feature.spectral_contrast(y=y, sr=sr)
                spr = np.mean(spr, axis=1)

                # Tonnetz
                ton = lb.feature.tonnetz(y=y, sr=sr)
                ton = np.mean(ton, axis=1)

                # Zero-Crossing rate
                zcr = lb.feature.zero_crossing_rate(y)
                zcr = np.mean(zcr, axis=1)

                # Spectral centroid
                spc = lb.feature.spectral_centroid(y=y, sr=sr)
                spc = np.mean(spc, axis=1)

                # Spectral bandwidth
                spb = lb.feature.spectral_bandwidth(y=y, sr=sr)
                spb = np.mean(spb, axis=1)

                arr = list(np.hstack((mfcc, chroma, spr, ton, zcr, spc, spb)))
                arr.append(i)
                data.append(arr)
                if j % 10 == 0:
                    print(f"{j}/100 files done!")
            except Exception:
                print(f"{j} from {i} genre skipped!")

    # Consolidate all genres' data into a single df.
    # generate column names:
    mfcc = [f'mfcc_{i+1}' for i in range(20)]
    chroma = [f'chroma_{i+1}' for i in range(12)]
    contrast = [f'spectral_contrast_{i+1}' for i in range(7)]
    tonnetz = [f'tonnetz_{i+1}' for i in range(6)]

    # consolidate:
    columns = mfcc + chroma + contrast + tonnetz + \
        ['zero_crossing_rate', 'spectral_centroid', 'spectral_bandwidth', 'genre']

    # create a df:
    df = pd.DataFrame(data, columns=columns)
    print(df)

    # Shuffle and Split data:
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for tr, te in split.split(df.drop('genre', axis=1), df['genre'].copy()):
        train = df.iloc[tr]
        test = df.iloc[te]

    # save training and testing data:
    train.to_csv('train1.csv', index=False)
    test.to_csv('test1.csv', index=False)

    # Seperate features and labels:
    features = train.drop('genre', axis=1)
    labels = train['genre'].copy()

    # Construct a pipeline to scale features:
    pipeline = Pipeline([
        ('scale', StandardScaler())
    ])

    # Scale features:
    features = pipeline.fit_transform(features)

    # Train model:
    model = SVC()
    model.fit(features, labels)

    # Save model and pipeline:
    joblib.dump(pipeline, 'pipeline.pkl')
    joblib.dump(model, 'model.pkl')

else:
    # Inference:
    model = joblib.load('model.pkl')
    pipeline = joblib.load('pipeline.pkl')
    data = pd.read_csv('test1.csv')
    features = pipeline.transform(data.drop('genre', axis=1))
    labels = data['genre'].copy()
    predictions = model.predict(features)
    print(predictions)

    # Check accuracy:
    accuracy = accuracy_score(labels, predictions)
    print("Accuracy:", accuracy * 100)
