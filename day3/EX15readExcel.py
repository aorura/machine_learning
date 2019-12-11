import pandas as pd
import numpy as np

df = pd.read_csv('data/ex1.csv')
print(df)

df2=pd.read_csv('data/ex2.csv', header=None)
print('\n', df2)

df2=pd.read_csv('data/ex2.csv', names=['one','two','three','four','msg'])
print('\n', df2)

df2=pd.read_csv('data/ex2.csv', names=['one','two','three','four','msg'],index_col='msg')
print('\n', df2)

df3=pd.read_csv('data/csv_mindex.csv',index_col=['key1','key2'])
print('\n',df3)

df4 = pd.read_csv('ex4.csv', skiprows=[0,2,3])
print('\n',df4)

