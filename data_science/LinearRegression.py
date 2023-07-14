import numpy
from sklearn.linear_model import LinearRegression
f,n  = map(int,input().split())
train  = numpy.array([input().split() for _ in range(n)],float)
t = int(input())
test  = numpy.array([input().split() for _ in range(t)],float)

X_tr = train[:,:f]
Y_tr = train[:,f]

clf = LinearRegression()
mod = clf.fit(X_tr,Y_tr)

pred = clf.predict(test)

for i in pred:
    print(i)

import numpy
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing as pp

f,n  = map(int,input().split())
train  = numpy.array([input().split() for _ in range(n)],float)
t = int(input())
test  = numpy.array([input().split() for _ in range(t)],float)

X_tr = train[:,:f]
Y_tr = train[:,f]

clf = LinearRegression()
#mod = clf.fit(X_tr,Y_tr)
#pred = clf.predict(test)

XtoP = pp.PolynomialFeatures(3, include_bias=False)
mod = clf.fit(XtoP.fit_transform(X_tr), Y_tr)

pred = mod.predict(XtoP.fit_transform(test))

for i in pred:
    print(i)


import json
import os
import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def loadTestingData():
    x = []
    n = int(input())
    
    for i in range(n):
        item = json.loads(input())
        del item['serial']
        x.append(list(item.values()))
    return np.array(x)

def loadTrainingData():
    x = []
    y = []
    with open('training.json') as f:
        lines = f.readlines()#[0:5]
        lines.pop(0)
        train_data = []
        for line in lines:
            item = json.loads(line)
            train_data.append(item)
            y.append([item['Mathematics']])
            
            del item['Mathematics']
            del item['serial']
            
            x.append(list(item.values()))
    return train_data,np.array(x), np.array(y)
    
def main():
    xTrain, yTrain = loadTrainingData()
    xTest = loadTestingData()
    
    model = LinearRegression().fit(xTrain, yTrain)
    result = model.predict(xTest).flatten()
    
    for item in result:
        print(round(item))
    
# if __name__ == "__main__":
#     main()