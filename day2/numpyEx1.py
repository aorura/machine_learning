import numpy as np

data1 = [1,2,3,4]
arr1 = np.array(data1)
print('data1: ', data1)
print('arr1: ', arr1)

data2=[[1,2,3,4],[1,2,3,4]]
arr2=np.array(data2, dtype=np.float32)
print('arr2:\n ', arr2)
print('dim: ', arr2.ndim)
print('shape: ', arr2.shape)
print('dtype: ', arr2.dtype)

n_string = np.array(['1.23','9.6','42'],dtype=np.string_)
print(n_string)
t_data=n_string.astype(np.float32)
print(t_data)