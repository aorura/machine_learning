import numpy as np
import pandas as pd
'''
obj=pd.Series(range(4),index=list('dabc'))
print(obj.sort_index(),'\n')

frame=pd.DataFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=list('dabc'))
print(frame.sort_index(),'\n')
print(frame.sort_index(axis=1),'\n')
print(frame.sort_index(axis=1,ascending=False),'\n')

print(obj.sort_values())
'''
frame2=pd.DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
print('\n',frame2)
print('\n',frame2.sort_values(by='b'))
print('\n',frame2.sort_values(by='a'))
print('\n',frame2.sort_values(by=['a','b']))

np.random.seed(777)
df=pd.DataFrame(np.random.randn(1000,4),columns=list('abcd'))
print(df)
print('\n',df.sum(axis=0))
print('\n',df.sum(axis=1))
print('\n',df.mean(axis=1))
print('\n',df.describe())
print('\n',df.info())

print('\n',df.head(10))
print('\n',df.tail(10))
