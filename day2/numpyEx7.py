import numpy as np

xarr = np.array([1.1,1.2,1.3,1.4,1.5])
yarr = np.array([2.1,2.2,2.3,2.4,2.5])
cond = np.array([True, False, True, True, False])

print([ x if c else y for x, y, c in zip(xarr, yarr, cond)])

result2=np.where(cond,xarr,yarr)
print('result2: ', result2)

np.random.seed(777)
arr=np.random.randn(4,4)
print('\n',arr)
print('\n',np.where(arr>0,2,-2))
print('\n',np.where(arr>0,2,arr))

arr=np.random.randn(5,4)
print('\n',arr)
print('\nmean1: ', arr.mean())
print('\nmean2: ', np.mean(arr))
print('\nsum: ', arr.sum())

print('\n', arr.mean(axis=1))
print('\n', arr.sum(axis=0))

arr=np.array([0,1,2,3,4,5,6,7])
print('\n', arr.cumsum())

arr=np.array([[0,1,2],
              [3,4,5],
              [6,7,8]])

print('\n',arr.cumsum(axis=0))
print('\n',arr.cumprod(axis=1))
