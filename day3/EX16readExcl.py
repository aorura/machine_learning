import numpy as np
import pandas as pd

data=pd.read_csv('data/ex6.csv',nrows=10)
#print('\n',data)

chunker = pd.read_csv('data/ex6.csv',chunksize=1000)
tot=pd.Series([])


for piece in chunker:
    tot = tot.add(piece['key'].value_counts(),fill_value=0)
    print(tot)
    break

tot=tot.sort_values(ascending=False)
print('\n',tot[:10])
