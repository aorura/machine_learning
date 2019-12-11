import numpy as np

arr1 = np.arange(1,7).reshape(2,3)
arr2 = np.arange(7,13).reshape(2,3)

print(arr1,'\n')
print(arr2)

print('\n', np.concatenate([arr1,arr2],axis=0))
print('\n', np.concatenate([arr1,arr2],axis=1))

print('\n', np.vstack((arr1, arr2)))
print('\n', np.hstack((arr1, arr2)))


arr3 = np.arange(6)
arr4 = np.arange(6).reshape(3,2)
arr5 = np.random.randn(3,2)
print('\n',arr3)
print('\n',arr4)
print('\n',arr5)
print('\n', np.r_[arr4,arr5])
print('\n', np.c_[arr4,arr5])
print('\n', np.c_[np.r_[arr4,arr5],arr3])
