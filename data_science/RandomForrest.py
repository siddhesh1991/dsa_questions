import json, sys
import pandas
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, ExtraTreesClassifier, RandomForestRegressor


with sys.stdin as fil:
    next(fil)
    test_frame = pandas.DataFrame(json.loads(line) for line in fil)

with open('training.json', 'r') as fil:
  next(fil)
  train_frame = pandas.DataFrame(json.loads(line) for line in fil)

train_y = train_frame.Mathematics.values
train_frame.drop(['Mathematics', 'serial'], axis = 1, inplace = True)
train_frame.fillna(train_frame.mean(), inplace = True)
test_frame.drop(['serial'], axis = 1, inplace = True)
test_frame.fillna(test_frame.mean(), inplace = True)

train_x = train_frame.values
test_x = test_frame.values

scaler = StandardScaler()
train_x = scaler.fit_transform(train_x)
test_x = scaler.transform(test_x)

model = RandomForestRegressor(random_state = 42, n_estimators = 50)

model.fit(train_x, train_y)
predictions = model.predict(test_x)
for pred in predictions:
    print int(round(pred))