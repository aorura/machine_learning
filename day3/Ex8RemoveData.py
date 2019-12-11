import pandas as pd
import numpy as np

obj=pd.Series(np.arange(5.),index=['a','b','c','d','e'])
print('\n',obj)
new_obj=obj.drop('c')
print('\n',new_obj)
print('\n',obj.drop(['d','c']))

data=pd.DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colorado','Utah','NewYork'],columns=['one','two','three','four'])
print('\n',data)
print('\n',data.drop(['Colorado','Ohio']))
print('\n',data.drop(['two','four'],axis='columns'))