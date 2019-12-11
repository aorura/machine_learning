import pandas as pd
import numpy as np

obj = pd.Series([4,7,-5,3],index=['d','b','a','c'])
print(obj)

obj2=obj.reindex(['a','b','c','d','e'])
print('\n', obj2)

obj3=pd.Series(['blue','purple','yellow'],index=[0,2,4])
print('\n',obj3)

obj4=obj3.reindex(range(6),method='ffill')
print('\n',obj4)

frame = pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=['First','Second','Third'])

print('\n', frame)
frame2=frame.reindex(['a','b','c','d'])
print('\n',frame)
frame3=frame.reindex(columns=['one','Second','Third'])
print('\n',frame3)