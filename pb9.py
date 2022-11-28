#getting data from specific column

import pandas as pd 

data = pd.read_csv(r'c:\pythoncode\Giants.csv')
df = pd.DataFrame(data, columns=['CEO', 'Established'])
print(df)