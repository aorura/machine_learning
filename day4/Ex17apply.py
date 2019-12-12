import pandas as pd
import numpy as np

tips = pd.read_csv('data/tips.csv')

tips['tip_pct'] = tips['tip'] / tips['total_bill']

def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]

print('\n1.', top(tips,n=6), '\n')
print('\n2.',tips.groupby('smoker').apply(top),'\n')
print('\n3.', tips.groupby(['smoker','day']).apply(top,n=1,column='total_bill'),'\n')

result=tips.groupby('smoker')['tip_pct'].describe()
print('\n4.',result,'\n')
print('\n5.',result.unstack(),'\n')

print('\n6.', tips.pivot_table(index=['sex','day'],columns='smoker'))
print('\n7.', tips.pivot_table(index=['sex','day'],columns='smoker',aggfunc=len))
print('\n8.', tips.pivot_table('tip_pct', index=['sex','day'],columns='smoker',aggfunc=len))

frame=pd.DataFrame({'a':range(7),'b':range(7,0,-1),'c':['one','one','one','two','two','two','two'],'d':[0,1,2,0,1,2,3]})
print('\n9.',frame)
frame2=frame.set_index('c')
print('\n10.',frame2)
frame3=frame.set_index(['c','d'])
print('\n11.',frame3)