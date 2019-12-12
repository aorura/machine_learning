import pandas as pd
import numpy as np

np.random.seed(12345)
data=pd.DataFrame(np.random.randn(1000,4))
print('\n', data.describe(),'\n')

#data[data>3]=3
#data[data<-3]=-3

data[(np.abs(data) > 3)] = np.sign(data)*3
print('\n',data.describe(),'\n')

