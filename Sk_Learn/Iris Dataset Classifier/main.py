from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# load the dataset
df_train = pd.read_excel("iris_data.xlsx")
df_test = pd.read_excel("iris_test.xlsx")

# clean the data
df_train.dropna(inplace=True)

# train model
x = df_train.drop("class", axis=1)
y = df_train['class']
model = RandomForestClassifier()  # using random forest
model.fit(x.values, y)
model2 = DecisionTreeClassifier()  # using decision tree
model2.fit(x.values, y)

# test the model
x2 = df_test.drop('class', axis=1)
y2 = df_test['class']
predict1 = model.predict(x2.values)
predict2 = model2.predict(x2.values)
print(predict1)
print(predict2)

# Check accuracy
# Random forest
count = 0
l1 = len(y2)
for i in range(l1):
    if y2[i] == predict1[i]:
        count += 1
print(f"Random forest classifier: {(count/l1) * 100}")

# Decision tree
count = 0
for i in range(l1):
    if y2[i] == predict2[i]:
        count += 1
print(f"Decision tree classifier: {(count/l1) * 100}")
