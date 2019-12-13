import pandas as pd
import numpy as np

p = pd.Period('2017',freq='A-DEC')
print(p)
print(p.asfreq('M',how='start'))
print(p.asfreq('M', how='end'))

p2 = pd.Period('2017',freq='A-DEC')
print(p2)
print(p2.asfreq('M',how='start'))
print(p2.asfreq('M', how='end'))


ts = pd.Series(np.random.randn(4), index=pd.date_range('2006','2010', freq='A-DEC'))
print('\n', ts)
print('\n',ts.asfreq('M',how='start'))

p3 = pd.Period('2012Q4', freq='Q-DEC')
print('\n', p3)
print('\n', p3.asfreq('M',how='end'))