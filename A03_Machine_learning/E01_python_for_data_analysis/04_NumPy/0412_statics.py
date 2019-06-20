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

# 计算每行的平均值
print(arr.mean(axis=0))
# 12 / 3
# 15 / 3
# 18 / 3

# 计算每列的平均值
print(arr.mean(axis=1))
# 6 / 3
# 15 / 3
# 24 / 3

'''
arr.cumsum() 累加值計算
'''
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr.cumsum())
print(arr.cumprod())

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr)
print(arr.cumsum(axis=0))
print(arr.cumsum(axis=1))

print(arr.cumprod(axis=0))
print(arr.cumprod(axis=1))

'''
用在布林值陣列的方法
'''
arr = np.random.randn(10)
print(arr)
print((arr > 0).sum())

bools = np.array([False, False, True, False])
print(bools.any())  # any用于测试数组中是否存在一个或多个True
print(bools.all())  # all则检查数组中所有值是否都是True

'''
排序
'''
# 單緯陣列 排序
print(arr)
t = arr.sort()
print(arr)

# 多緯陣列 排序
arr = np.random.randn(5, 3)
print(arr)

arr.sort(0)
print(arr)

arr.sort(1)
print(arr)
'''
唯一化以及其它的集合逻辑
'''
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
unique_name = np.unique(names)
print(unique_name)
print(sorted(set(names)))

ints = np.array([3, 3, 2, 2, 1, 1, 4, 4])
unique_ints = np.unique(ints)
print(unique_ints)

#集合函數
values = np.array([6, 0, 0, 3, 2, 5, 6])
in1d = np.in1d(values, [2, 3, 4])
print(in1d)


