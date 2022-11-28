import pandas as pd
df = pd.read_csv('online-retail.csv')
df.head()#print the first n rows in the data frame [default n=5]

print(df)
df['LinePrice'] = df['Quantity'] * df['UnitPrice']
df.head()

print(df)