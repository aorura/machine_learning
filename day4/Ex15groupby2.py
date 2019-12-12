import numpy as np
import pandas as pd

people=pd.DataFrame(np.random.randn(5,5), columns=list('abcde'),index=['Joe','Steve','Wes','Jim','Travis'])
people.loc[2:3,['b','c']]=np.nan
print(people,'\n')
mapping={'a':'red','b':'red','c':'blue','d':'blue','e':'red'}
by_column=people.groupby(mapping,axis=1)
print('\n', by_column.sum())

print('\n', people.groupby(len).sum())

key_list=['one','one','one','two','two']
print('\n',people.groupby([len,key_list]).sum())
