import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr)

print(arr.mean())
print(np.mean(arr))
print(arr.sum())

print(arr.mean(axis=0))
12  # 计算每行的
15
18

print(arr.mean(axis=1))
6  # 计算每列的
15
24
