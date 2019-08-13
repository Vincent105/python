import numpy as np

grid = np.arange(1, 10).reshape((3, 3))
print(grid)

x = np.array([1, 2, 3])
print(x)
print(x.reshape((1, 3)))
print(x[np.newaxis, :], "newaxis关键字获得的行向量")
print(x.reshape((3, 1)))
print(x[:, np.newaxis], "newaxis关键字获得的列向量")
