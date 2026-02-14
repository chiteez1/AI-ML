import numpy as np
import pandas as pd
import os
import joblib
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor

# House prediction project using scikit learn. Let's get into it!


# Define file names.
MODEL_FILE = "model.pkl"
PIPELINE_FILE = 'pipeline.pkl'


# Check if model file exists:
if not os.path.exists(MODEL_FILE):

    # Spilt training and testing data:
    df = pd.read_csv("./data.csv")


    # Create a stratified split based on income category:
    # Create income column:
    df['income_cat'] = pd.cut(df['median_income'],
                              bins=[0., 1.5, 3.0, 4.5, 6, np.inf],
                              labels=[1, 2, 3, 4, 5])

    # Stratify data:
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for tr, ts in split.split(df, df['income_cat']):
        train = df.loc[tr].drop("income_cat", axis=1)
        test = df.loc[ts].drop("income_cat", axis=1)

    # Save testing data:
    test.to_csv("test.csv", index=False)

    # Seperate features and labels:
    labels = train['median_house_value'].copy()
    features = train.drop('median_house_value', axis=1)

    # Seperate numerical and categorical columns:
    num_att = features.drop('ocean_proximity', axis=1).columns.tolist()
    cat_att = ['ocean_proximity']


    # Construct pipeline:
    # Numerical pipeline:
    num_ppl = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('scaler', StandardScaler())
    ])

    # Categorical pipeline:
    cat_ppl = Pipeline([
        ("onehot", OneHotEncoder())
    ])

    # Full pipeline:
    f_ppl = ColumnTransformer([
        ('num', num_ppl, num_att),
        ('cat', cat_ppl, cat_att)
    ])


    # Transform!:
    features = np.array(f_ppl.fit_transform(features))


    # Train data on random forest:
    model = RandomForestRegressor(random_state=42)
    model.fit(features, labels)


    # Save the model and pipeline:
    joblib.dump(model, MODEL_FILE)
    joblib.dump(f_ppl, PIPELINE_FILE)

# If yes:
else:
    # Inference:
    # Load model & pipeline:
    model = joblib.load('model.pkl')
    pipeline = joblib.load('pipeline.pkl')


    # Load Data:
    test = pd.read_csv("test.csv")
    test = test.drop('median_house_value', axis=1)


    # Transform data:
    features = pipeline.transform(test) 


    # Predict output:
    predictions = model.predict(features)


    # Save the output in a file:
    test['median_house_value'] = predictions
    test.to_csv('output.csv', index=False)
