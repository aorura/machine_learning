import numpy as np

arr = np.arange(10)
print(arr[4])
print(arr[4:])

data = np.array([[3,1,7],[2,5,4],[9,22,33]])
print('\n',data[1,1])
print('\n',data[1][1])
print('\n',data[1:,1:])
print('\n',data[1:][1:])
