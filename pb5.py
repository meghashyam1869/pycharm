import pandas as pd

#using the dict data --->DF
data = {'Country': ['Belgium', 'India', 'Brazil'],'Capital':['Brussels', 'New Delhi', 'Brazilia'],'Population': [11190846, 1303171035, 207847528]}
#df = pd.DataFrame(data,columns=['Country', 'Capital', 'Population'])
df = pd.DataFrame(data,columns=['Customer-Region', 'City', 'Population'])
print (df)