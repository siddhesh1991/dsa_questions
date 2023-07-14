# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

dota = pd.read_csv('trainingdata.txt', header=None)

team1wins = dota[dota[10] == 1]
team1wins = team1wins.drop(columns=[5, 6, 7, 8, 9, 10])
team1wins = pd.DataFrame(team1wins.values.flatten())
charactersTeam1 = team1wins[0].value_counts()

team2wins = dota[dota[10] == 2]
team2wins = team2wins.drop(columns=[0, 1, 2, 3, 4, 10])
team2wins = pd.DataFrame(team2wins.values.flatten())
charactersTeam2 = team2wins[0].value_counts()

characterWins1 = pd.DataFrame(charactersTeam1)
characterWins2 = pd.DataFrame(charactersTeam2)
characterWins = pd.merge(characterWins1, characterWins2, left_index=True, right_index=True, how='outer' )
characterWins.rename(columns={'0_x':'Team_One','0_y':'Team_Two'}, inplace=True)
characterWins['Total'] = characterWins['Team_One'] + characterWins['Team_Two']

dota2 = dota.drop(columns=10)
dota2 = pd.DataFrame(dota2.values.flatten())
totalPlayedChar = dota2[0].value_counts()
totalPlayedChar = pd.DataFrame(totalPlayedChar)
characterWins = pd.merge(characterWins, totalPlayedChar, left_index=True, right_index=True, how='outer' )
characterWins['Win_Rate'] = characterWins['Total'] / characterWins[0]
characterWins.drop(columns=['Team_One','Team_Two','Total',0], inplace=True)
winRate = characterWins['Win_Rate'].to_dict()
dota[0] = dota[0].map(winRate)
dota[1] = dota[1].map(winRate)
dota[2] = dota[2].map(winRate)
dota[3] = dota[3].map(winRate)
dota[4] = dota[4].map(winRate)
dota[5] = -dota[5].map(winRate)
dota[6] = -dota[6].map(winRate)
dota[7] = -dota[7].map(winRate)
dota[8] = -dota[8].map(winRate)
dota[9] = -dota[9].map(winRate)

target = dota[10]
dota.drop(columns=10, inplace=True)

# User input
K = int(input())
userInput = pd.DataFrame([[j for j in input().split(',')] for i in range(K)])
userInput[0] = userInput[0].map(winRate)
userInput[1] = userInput[1].map(winRate)
userInput[2] = userInput[2].map(winRate)
userInput[3] = userInput[3].map(winRate)
userInput[4] = userInput[4].map(winRate)
userInput[5] = -userInput[5].map(winRate)
userInput[6] = -userInput[6].map(winRate)
userInput[7] = -userInput[7].map(winRate)
userInput[8] = -userInput[8].map(winRate)
userInput[9] = -userInput[9].map(winRate)

model = RandomForestClassifier(n_estimators=150, random_state=0)
model.fit(dota, target)

prediction = model.predict(userInput)
for i in prediction:
    print(i)



# Enter your code here. Read input from STDIN. Print output to STDOUT
import csv, sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier

columns = ['heroA_'+str(i) for i in range(5)]+['heroB_'+str(i) for i in range(5)]+['winner']
train = pd.read_csv("trainingdata.txt", names = columns)

y_train = train['winner'].replace({1:False, 2:True}) #convert to binary
X_train = train.drop('winner', axis=1)
X_train_A = X_train[['heroA_'+str(i) for i in range(5)]]
X_train_B = X_train[['heroB_'+str(i) for i in range(5)]]

mlb1 = MultiLabelBinarizer()
X_train_sparseA = mlb1.fit_transform(X_train_A.values)
mlb2 = MultiLabelBinarizer()
X_train_sparseB = mlb2.fit_transform(X_train_B.values)
# print(X_train_sparseA.shape)
# print(X_train_sparseB.shape)
# print(len(mlb1.classes_))
# print(len(mlb2.classes_))
X_train = pd.concat([
    pd.DataFrame(X_train_sparseA, columns=["heroesA_"+c for c in mlb1.classes_]),
    pd.DataFrame(X_train_sparseB, columns=["heroesB_"+c for c in mlb2.classes_])],
    axis=1)

# clf = RandomForestClassifier(n_estimators=100,oob_score=True)
# clf.fit(X_train, y_train)
# print(clf.score(X_train, y_train))

X_test_A = []
X_test_B = []
for idx,line in enumerate(csv.reader(sys.stdin)):
    if idx>0:
        X_test_A.append(line[:5])
        X_test_B.append(line[5:])

# print(np.array(X_test_A).shape)
X_test=pd.concat([
    pd.DataFrame(mlb1.transform(X_test_A),columns=["heroesA_"+c for c in mlb1.classes_]),
    pd.DataFrame(mlb2.transform(X_test_B),columns=["heroesB_"+c for c in mlb2.classes_])
    ],axis=1) 

# # print(X_test.head())
# pred = clf.predict(X_test)

# for p in pred:
#     print(p+1)

# columns = ['hero_'+str(i) for i in range(10)]+['winner']
# train = pd.read_csv("trainingdata.txt", names = columns).head()

# y_train = train['winner'].replace({1:False, 2:True}) #convert to binary

# X_train = train.drop('winner', axis=1)
# X_train_B = X_train.iloc[:,5:]
# mlb1 = MultiLabelBinarizer()
# X_train_sparse = mlb1.fit_transform(X_train.values)

# X_train_sparse = pd.DataFrame(X_train_sparse, columns=[c for c in mlb1.classes_])

# for row_num,row in enumerate(X_train_B.values):
#   for val in row:
#     X_train_sparse.loc[row_num,val]=-1
