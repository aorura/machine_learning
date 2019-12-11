import numpy as np
import pandas as pd

np.random.seed(777)
df1 = pd.DataFrame(np.random.randn(2,2),index=['first', 'second'],columns=['one','two'])

print(df1)

df2 = pd.DataFrame(np.random.randn(2,2),columns=['one','two'])

print('\n', df2)

data={'state':['ohio','LA','Nevada','Nevada','Nevada','Nevada'],'year':[2000,2001,2002,2002,2002,2002],'pop':[1.5,1.7,1.8,1.8,1.8,1.8]}
frame=pd.DataFrame(data)
print('\n', frame)

frame2 = pd.DataFrame(data,columns=['year','state','pop','dept'],index=['one','two','three','four','five','six'])

print('\n',frame2)
print('\n',frame2['state'])
print('\n',frame2.state)
print('\n',frame2.loc['two'])

frame2.index.name='index'
frame2.columns.name='info'
print('\n',frame2)
