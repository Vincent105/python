import numpy as np

# 1d slice
arr = np.array([0,  1,  2,  3,  4, 64, 64, 64,  8,  9])
print(arr[1:6])

# 2d slice
arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr2d[:2])
print(arr2d[:2, 1:])
print(arr2d[1, :2])  # 选取第二行的前两列：
print(arr2d[:2, 2])  # 还可以选择第三列的前两行：
print(arr2d[:, :1])  # 只对高维轴进行切片

# 对切片表达式的赋值操作也会被扩散到整个选区：
arr2d[:2, 1:] = 0
print(arr2d)