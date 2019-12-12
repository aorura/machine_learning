import pandas as pd
import numpy as np

data=pd.DataFrame(np.arange(6).reshape(2,3),index=pd.Index(['Ohio','Texas'],name='state'),columns=pd.Index(['one','two','three'],name='number'))

print(data)
result=data.stack()
print('\n',result)
print('\n',result.unstack())
print('\n',result.unstack(level=0))
print('\n',result.unstack('state'))