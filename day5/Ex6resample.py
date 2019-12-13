import pandas as pd
import numpy as np

ts = pd.Series(np.arange(12),index=pd.date_range('1/1/2000', periods=12,freq='T'))
print(ts)
print('\n', ts.resample('5min').sum())
print('\n', ts.resample('5min', closed='right').sum())
print('\n', ts.resample('5min', closed='right', label='right').sum())

frame = pd.DataFrame(np.random.randn(2,3), index=pd.date_range('1/1/2000',periods=2, freq='W-WED'),columns=['Colorado','NewYork','Ohio'])
print('\n',frame)
print('\n', frame.resample('D').ffill())
print('\n', frame.resample('D').ffill(limit=2)) #limit : n개만큰 앞에 값으로 채우기

