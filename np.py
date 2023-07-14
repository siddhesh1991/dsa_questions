import numpy as np
A = np.array([[1,2,2],[4,4,4],[7,8,9]])
B = np.array([[7,8,9],[4,4,4],[1,2,3]])
print('A:')
print(A)
print('B:')
print(B)
print()

# Matrix multiplication
print('A*B:')
print(A*B)
print()

# Inverse
print('A^{-1}:')
print(np.linalg.inv(A))
print()

# Solve Linear equation
y = np.array([10,20,30])
print('Solution to Ax=[10,20,30]')
print(np.linalg.solve(A,y))

import pandas as pd

transactions = {"transaction_id" : [1, 2, 3, 4, 5], "product_id" : [101, 102, 103, 104, 105], "amount" : [3, 5, 8, 3, 2]}
products = {"product_id" : [101, 102, 103, 104, 105], "price" : [20.00, 21.00, 15.00, 16.00, 52.00]}
df_transactions = pd.DataFrame(transactions)
df_products = pd.DataFrame(products)

(df_transactions
.merge(df_products, on = "product_id", how ="left")
.assign(value = lambda x: x.price * x.amount)
.query("value > 100")
)


import pandas as pd
students = {"name" : ["Tim Voss", "Nicole Johnson", "Elsa Williams", "John James", "Catherine Jones"], "age" : [19, 20, 21, 20, 23], "favorite_color" : ["red", "yellow", "green", "blue", "green"], "grade" : [91, 95, 82, 75, 93]}
students_df = pd.DataFrame(students)

students_df.query("((favorite_color == 'green') or (favorite_color == 'red')) and grade > 90  ")


import pandas as pd

addresses = {"address": ["4860 Sunset Boulevard, San Francisco, 94105", "3055 Paradise Lane, Salt Lake City, 84103", "682 Main Street, Detroit, 48204", "9001 Cascade Road, Kansas City, 64102", "5853 Leon Street, Tampa, 33605"]}

cities = {"city": ["Salt Lake City", "Kansas City", "Detroit", "Tampa", "San Francisco"], "state": ["Utah", "Missouri", "Michigan", "Florida", "California"]}

df_addresses = pd.DataFrame(addresses)
df_cities = pd.DataFrame(cities)


def complete_address(df_addresses, df_cities):
    df_addresses[['street', 'city', 'zipcode']] = df_addresses['address'].str.split(', ', expand=True)
    df_addresses = df_addresses.drop(['address'], axis=1)
    df_addresses = df_addresses.merge(df_cities, on="city")
    df_addresses['address'] = df_addresses[['street', 'city', 'state', 'zipcode']].agg(', '.join, axis=1)
    df_addresses = df_addresses.drop(['street', 'city', 'state', 'zipcode'], axis=1)
    return df_addresses
    