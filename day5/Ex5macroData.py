import pandas as pd
import numpy as np

data = pd.read_csv('data/macrodata.csv',parse_dates=True)
print('\n', data.year)

index = pd.PeriodIndex(year=data.year,quarter=data.quarter,freq='Q-DEC')
print('\n', index)
data.index=index
print('\n', data)

