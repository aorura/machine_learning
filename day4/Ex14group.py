import numpy as np
import pandas as pd

df = pd.DataFrame({'key1':['a','a','b','b','a'],
                   'key2':['one','two','one','two','one'],
                   'data1':np.random.randn(5),
                   'data2':np.random.randn(5)})
print('\n',df,'\n')
grouped=df['data1'].groupby(df['key1'])
print(grouped.mean())

means = df['data1'].groupby([df['key1'],df['key2']]).mean()
print('\n',means)
print('\n',means.unstack())
print('\n',means.unstack('key1'))

for name, group in df.groupby('key1'):
    print('name:', name)
    print(group, '\n')


for (k1, k2), group in df.groupby(['key1','key2']):
    print('name:', k1,k2)
    print(group, '\n')

pieces = dict(list(df.groupby('key1')))
print('\n',pieces['b'])

print('\n\n---\n\n', dict(list(df.groupby('key1'))))