# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.holtwinters import ExponentialSmoothing

n = int(input())

data = []
for _ in range(n):
    data.append(input())

visitors = np.array([int(row) for row in data])

model = ExponentialSmoothing(visitors, trend="add", damped=True, seasonal="add", seasonal_periods=7)
results = model.fit()

forecasts = results.forecast(30)
for predcited in forecasts:
    print(predcited)



import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor

n = int(raw_input())
data = []
for i in xrange(n):
    y = int(raw_input())
    data.append([i, y])

df = pd.DataFrame(data, columns=['day', 'y'])
df['day_sq'] = df['day'] ** 2
df['week_sin'] = np.sin(2 * np.pi * df['day'] / 7)
df['week_cos'] = np.cos(2 * np.pi * df['day'] / 7)
df['2week_sin'] = np.sin(2 * np.pi * df['day'] / 14)
df['2week_cos'] = np.cos(2 * np.pi * df['day'] / 14)
df['year_sin'] = np.sin(2 * np.pi * df['day'] / 250)
df['year_cos'] = np.cos(2 * np.pi * df['day'] / 250)
X_train = df[['day', 'week_sin', 'week_cos', '2week_sin', '2week_cos', 'year_sin', 'year_cos']].values
y_train = df['y'].values

df_test = pd.DataFrame(np.arange(n, n + 30), columns=['day'])
df_test['day_sq'] = df_test['day'] ** 2
df_test['week_sin'] = np.sin(2 * np.pi * df_test['day'] / 7)
df_test['week_cos'] = np.cos(2 * np.pi * df_test['day'] / 7)
df_test['2week_sin'] = np.sin(2 * np.pi * df_test['day'] / 14)
df_test['2week_cos'] = np.cos(2 * np.pi * df_test['day'] / 14)
df_test['year_sin'] = np.sin(2 * np.pi * df_test['day'] / 250)
df_test['year_cos'] = np.cos(2 * np.pi * df_test['day'] / 250)
X_test = df_test[['day', 'week_sin', 'week_cos', '2week_sin', '2week_cos', 'year_sin', 'year_cos']].values

model = LinearRegression()
# model = RandomForestRegressor(n_estimators=100, max_depth=10)
# model = Ridge(alpha=100.0)
y_test = model.fit(X_train, y_train).predict(X_test)
for a in y_test:
    print(np.nan)

l = np.array(l)
xl = l[:,0]
yl = l[:,1]

from scipy import interpolate
ir = interpolate.interp1d(xl,yl,fill_value='extrapolate')
res = ir(range(n+1,n+13))
for x in res:
    print(x)


## Temprature Predict
n_students = int(input())
col_names = input().split()
col_vals = []
for i in range(n_students):
    col_vals.append(input().split())


import pandas as pd

df = pd.DataFrame(col_vals, columns=col_names, index=range(n_students))
df.tmax = pd.to_numeric(df.tmax, errors="coerce")
df.tmin = pd.to_numeric(df.tmin, errors="coerce")
df_nona = df.interpolate(method='polynomial', order=2)

outlist = df_nona.tmax[df.tmax.isnull()].tolist() + df_nona.tmin[df.tmin.isnull()].tolist()

for i in outlist:
    print(i)

data.tmax = data.tmax.apply( process_numeric )
data.tmin = data.tmin.apply( process_numeric )

#interpolation
data_predict = pd.concat([data.tmax.interpolate( method = 'cubic', order = 2 ), data.tmin.interpolate( method = 'cubic', order = 2) ], axis = 1)

