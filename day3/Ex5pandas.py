import pandas as pd
import numpy as np

ddata={'Ohio':35000, 'Texas':71000,'Oregon':16000}
obj=pd.Series(ddata)
print(obj)

obj2=pd.Series(ddata,index=['Califonia', 'Oregon','Texas'],dtype=np.float32)
print('\n', obj2)