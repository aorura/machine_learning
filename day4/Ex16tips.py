import pandas as pd
import numpy as np

tips = pd.read_csv('data/tips.csv')
print('\n', tips.info())
print('\n', tips.head())

tips['tip_pct'] = tips['tip'] / tips['total_bill']
print('\n\npark',tips.head())
grouped = tips.groupby(['sex','smoker'])
print('\n',grouped.mean())
print('\n',grouped.agg('mean'))
print('\n',grouped.agg(['mean','std']))
print('\n',grouped.agg({'tip':np.max,'size':'sum'}))
print('\n',grouped.agg({'tip_pct':['min','max','mean','std'],'size':'sum'}))

def peek_to_peek(gdata):
    return gdata.max() - gdata.min()
print('\n', grouped.agg(peek_to_peek))
