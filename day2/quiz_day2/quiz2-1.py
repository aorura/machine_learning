import numpy as np
np.random.seed(777)

data = np.random.randn(5,6)
print(data)

#a
print('\n',data.max())

#b
print('\n',data.sum(axis=1))

#c
print('\n',data.mean(axis=0))

#d
print('\n',data[np.argsort(data[:, 0])])

#e
print('\n',data[:, np.argsort(data[1, :])])
