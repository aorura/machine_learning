import numpy as np

np.random.seed(777)
arr = np.random.randn(100)
print((arr > 0).sum())


bools = np.array([[False, False, True, False],
                  [False, False, True, False]])

print(bools.any(axis=1))
print(bools.any(axis=0))
print(bools.all(axis=0))

data = np.random.randn(10,4)
data = data * 2
print('\n', data)
print('\n', data[(data > 2.5).any(axis=1)])

#sort
print('\nsort')
arr = np.random.randn(5,3)
print('\n', arr)

arr.sort(axis=1)
print('\n',arr)
arr.sort(axis=0)
print('\n',arr)

#Relative Sort
print("\nRelative Sort")
values=np.array([5,0,1,3,2])
indexer = values.argsort()
print(indexer,'\n')
print(values[indexer], '\n')

arr = np.random.randn(3,5)
arr[0] = values
print(arr,'\n')
print(arr[:,arr[0].argsort()],'\n')
