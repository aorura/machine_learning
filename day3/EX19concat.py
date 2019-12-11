import numpy as np
import pandas as pd

s1 = pd.Series([0,1], index=['a','b'])
s2 = pd.Series([2,3,4], index=['c','d','e'])
s3 = pd.Series([5,6], index=['f','g'])

print('\ns1.', s1)
print('\ns2.', s2)
print('\ns3.', s3)

print('\n', pd.concat([s1,s2,s3]))
print('\n', pd.concat([s1,s2,s3], axis=1,sort=False),'\n')

s4 = pd.concat([s1*5,s3])
print('\n',s4)
print('\n',pd.concat([s1,s4],axis=1,sort=False))
print('\n',pd.concat([s1,s4],axis=1,join='inner'))