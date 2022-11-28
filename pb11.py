import pandas as pd

data = pd.read_excel(r'c:\pythoncode\companies.xlsx')
df = pd.DataFrame(data, columns=['CEO'])
print(df)