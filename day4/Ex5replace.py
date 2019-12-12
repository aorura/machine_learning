import numpy as np
import pandas as pd

data = pd.Series([1.,-999,2.,-999.,-1000.,3.,4.,10.,14.,20.,30.,40.])
print('\n', data, '\n')
print('\n', data.replace([-999,-1000], np.nan),'\n')
print('\n', data.replace({-999:np.nan,-1000:0}),'\n')

