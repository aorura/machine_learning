import numpy as np
import pandas as pd

data = pd.Series([1,np.nan,3.5,np.nan,7])
print('\n',data,'\n')
print('\n',data.dropna())
print('\n',data[data.notnull()],'\n')

np.random.seed(12345)
df=pd.DataFrame(np.random.randn(7,3))
df.iloc[:4,1]=np.nan
print('\n3',df)
df.iloc[:2,2]=np.nan
print('\n4',df)

print('\n1',df.fillna(0))
print('\n2',df.fillna({1:0.5,2:1.}))
print('\n3',df.fillna(method='backfill'))