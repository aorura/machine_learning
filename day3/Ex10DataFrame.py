import pandas as pd
import numpy as np

data=pd.DataFrame(np.arange(16).reshape(4,4),index=['Ohio', 'Colorado','Utah','NewYork'],
                  columns=['one','two','three','four'])
print(data)
print('\n', data.iloc[2, [3,0,1]])
print('\n', data.iloc[:, :3][data.three>5])