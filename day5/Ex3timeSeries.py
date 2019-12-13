from datetime import datetime
import pandas as pd
import numpy as np

np.random.seed(777)

dates = [datetime(2019,1,2),datetime(2019,1,7),datetime(2019,1,7),
         datetime(2019,1,8),datetime(2019,1,10),datetime(2019,1,12)]

ts=pd.Series(np.random.randn(6),index=dates)

print(ts)
print('\n',ts['1/10/2019'])
print('\n',ts['20190110'])

longData = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2015',periods=1000))
print('\n',longData)
print('\n',longData['2016'])
print('\n',longData['2016-05'])
print('\n',longData['2016-05-01':'2016-05-10'])

ldFrame = pd.DataFrame(np.random.randn(100,3),index=pd.date_range('1/1/2017',periods=100,freq='W-WED'),columns=['Ohio','Texas','Utah'])
print('\n',ldFrame)
print('\n',ldFrame.loc['2017-05']) #loc index에서 찾음

print('\n',pd.date_range(start='4/1/2012', periods=20))
print('\n',pd.date_range(end='4/1/2012', periods=20))
print('\n',pd.date_range(start='4/1/2012',end='12/1/2012',freq="BM")) # BM : bussiness monday
print('\n',pd.date_range(start='5/2/2012 12:56:31', periods=5, freq='4h'))
print('\n',pd.date_range(start='5/2/2012 12:56:31', periods=5, freq='1h30min'))
print('\n',pd.date_range(start='4/1/2012',end='12/1/2012',freq="WOM-2FRI")) # WOM-2FRI : 각 달의 2번째 금요일

