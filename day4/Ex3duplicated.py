import pandas as pd
import numpy as np

data=pd.DataFrame({'k1':['one']*3+['two']*4,'k2':[1,1,2,3,3,4,4]})

print('\n',data,'\n')
print('\n',data.duplicated(),'\n')
print('\n',data.drop_duplicates(),'\n')

data['v1']=range(7)
print('\n',data,'\n')
print('\n',data.drop_duplicates(['k1']),'\n')
print('\n',data.drop_duplicates(['k1','k2'],keep='last'),'\n')