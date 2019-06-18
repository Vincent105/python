import numpy as np

arr = np.empty((8, 4))
print(arr)

for i in range(8):
    arr[i] = i

print(arr)

print(arr[[4, 3, 0, 6]])

print(arr[[-1, -3, -5, -7]])

# 一次传入多个索引数组会有一点特别。它返回的是一个一维数组，其中的元素对应各个索引元组：
# 最终选出的是元素(1,0)、(5,3)、(7,1)和(2,2)。无论数组是多少维的，花式索引总是一维的。
arr = np.arange(32).reshape((8, 4))
print(arr)

print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])

# 花式索引跟切片不一样，它总是将数据复制到新数组中。

