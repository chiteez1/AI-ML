# Iris Classification Using Random Forest and Decision Tree

This project demonstrates a simple machine-learning workflow using **RandomForestClassifier** and **DecisionTreeClassifier** from **scikit-learn** to classify Iris flower species.  
The workflow includes loading data, preprocessing, training two models, testing, and manually calculating accuracy.

## Models Used

### 1. **Random Forest Classifier**
A robust ensemble learning method that builds multiple decision trees and averages their outputs to improve accuracy and prevent overfitting.

### 2. **Decision Tree Classifier**
A simple, interpretable model that splits data based on feature thresholds to classify samples.

## How It Works

1. **Load the datasets**
   - `iris_data.xlsx` for training  
   - `iris_test.xlsx` for testing

2. **Clean the data**
   - Remove missing values in the training set.

3. **Train the models**
   - Features (`x`): all columns except *class*  
   - Labels (`y`): the *class* column  
   - Train both Random Forest and Decision Tree models using the cleaned dataset.

4. **Test the models**
   - Predict classes for the test dataset.
   - Print predicted labels for both models.

5. **Manually check accuracy**
   - Loop through each prediction and compare it with the true label.
   - Calculate and print accuracy for both models.


## Requirements

#### Librabries/packages required:
1. scikit learn
1. pandas
1. openpyxl (required for reading .xlsx files with pandas)
#### Install required dependencies:

```bash
pip install pandas scikit-learn openpyxl
```

## Output

The script prints:

1. Predictions made by both models
3. Accuracy scores for:
    - Random Forest Classifier
    - Decision Tree Classifier

Example output:
``` sql
[ 'Iris-setosa' 'Iris-virginica' ... ]
[ 'Iris-setosa' 'Iris-virginica' ... ]
...
Random forest classifier: 96.67
Decision tree classifier: 93.33
```


## Conclusion
I created this project as a starting point for my journey into machine learning, and it turned out to be an incredibly enjoyable and rewarding experience. I encourage every beginner—just like me—to try building a project like this. It’s a great way to understand the fundamentals of machine learning while gaining hands-on experience that builds both confidence and curiosity.
