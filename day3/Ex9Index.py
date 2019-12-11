import pandas as pd
import numpy as np

obj=pd.Series(np.arange(4.), index=['a','b','c','d'])
print('\n',obj)
print('\n',obj['b'])
print('\n',obj[1])
print('\n',obj[2:4])
print('\n',obj[['b','a','d']])
print('\n',obj[[1,3]])
print('\n',obj[obj < 2])
print('\n',obj['b':'c'])
obj['b':'c'] = 5
print('\n',obj)
