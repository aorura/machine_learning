import pandas as pd
import numpy as np

obj = pd.Series([4,7,-5,3])
print('\n',obj)
print('\n',obj.values)
print('\n',obj.index)

'''
obj2 = pd.Series([4,7,-5,3],index=['d','b','a','c'])
print('\n',obj2)
print('\n',obj2.index)

print('\n',obj2['a'])
obj2['d']=6
print('\n', obj2[['c','a','d']])

print('\n', obj2[obj2>0])
print('\n',obj2*2)
print('\n',np.exp(obj2))
'''