import numpy as np

arr = np.arange(32)
print(arr)
arr2 = arr.reshape((8,4))
print('arr2:\n', arr2)
print('arr2:\n', arr2.T)    # transfer: 행과 열을 바꿈.