import pandas as pd
import numpy as np

a = pd.Series([np.nan,2.5,np.nan,3.5,4.5,np.nan],index=['f','e','d','c','b','a'])
b = pd.Series(np.arange(len(a),dtype=np.float32),index=['f','e','d','c','b','a'])

print(a,'\n')
print(b,'\n')
print('\n',a[:].combine_first(b[:]))

df1=pd.DataFrame({'a':[1.,np.nan,5.,np.nan],'b':[np.nan,2.,np.nan,6.],'c':range(2,18,4)})
df2=pd.DataFrame({'a':[5.,4.,np.nan,3.,7.],'b':[np.nan,3.,4.,6.,8.]})

print('\n',df1)
print('\n',df2)
print('\n',df1.combine_first(df2))