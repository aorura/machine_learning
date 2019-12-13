import pandas as pd
import numpy as np

years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']

data = pd.read_csv('data/yob1880.txt',names=columns)

print('1.')
print('\'n', data)

print('2.')
print('\n', data.head(10))
print('\n', data.tail(10))

print('3.')
print('\n', data['births'].groupby(data['sex']).sum())

print('4.')
for year in years:
    path = 'data/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
print('\n', pieces)

print('5.')
names = pd.concat(pieces,axis=0)
print(names)

print('6.')
birthsum=names.pivot_table(index=['year'],columns='sex',aggfunc=sum)
print('\n', birthsum)

print('7.')
import matplotlib.pyplot as plt
birthsum.plot(kind='bar')
#plt.show()

print('8.')
namesum=names.groupby(names['name']).sum()
#namesum['prop'] = namesum /namesum.sum()
print('\n', namesum)

print('9.')
print('\n', namesum['prop'].sort_values(ascending=False).head(1000))

