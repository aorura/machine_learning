import numpy as np

arr = np.arange(10)
print(arr,'\n')
print(np.sqrt(arr),'\n')

print(np.exp(arr),'\n')

np.random.seed(12345)
x = np.random.randn(8)
y = np.random.randn(8)

print(x,'\n')
print(y,'\n')
print(np.maximum(x,y),'\n')

arr = np.random.randn(7)*5
print(arr,'\n')
print(np.modf(arr),'\n')