import numpy as np
import pandas as pd

np.random.seed(777)
frame = pd.DataFrame(np.random.randn(4,3),columns=list('bde'),index=['Utah','Texas','Ohio','NewYork'])
print(frame)
#print('\n',np.abs(frame))

f=lambda x : x.max()-x.min()
print('\n',frame.apply(f,axis=0))

def f2(x):
    return pd.Series([x.min(),x.max()], index=['min','max'])

print('\n', frame.apply(f2,axis=0))
print('\n', frame.apply(f2,axis=1))

print('\n', f2(np.arange(6).reshape(3,2)))
