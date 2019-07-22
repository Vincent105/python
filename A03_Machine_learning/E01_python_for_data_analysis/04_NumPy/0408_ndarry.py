import numpy as np

arr = np.arange(15).reshape((3, 5))
print(arr)

# 特殊的T属性
print(arr.T)

# 利用np.dot计算矩阵内积
arr = np.random.randn(6, 3)
print(arr)

dot_result = np.dot(arr.T, arr)
print(dot_result)

arr = np.arange(16)
print(arr)
'''
transpose() 概念拆解… 2d
'''
x = np.arange(4).reshape((2, 2))
print(x)
print(x.transpose())

t1 = x.transpose((0, 1))
print(t1)

t2 = x.transpose((1, 0))
print(t2)

print(x[0][0])
print(x[0][1])
print(x[1][0])
print(x[1][1])

# 交換第0軸以及第1軸
print(x[0][0])
print(x[1][0])
print(x[0][1])
print(x[1][1])

'''
transpose() 概念拆解… 3d
'''
arr = np.arange(12).reshape((2, 2, 3))
print(arr)
print(arr[0][0][0])
print(arr[0][0][1])
print(arr[0][0][2])
print(arr[0][1][0])
print(arr[0][1][1])
print(arr[0][1][2])
print(arr[1][0][0])
print(arr[1][0][1])
print(arr[1][0][2])
print(arr[1][1][0])
print(arr[1][1][1])
print(arr[1][1][2])

# 交換第0軸以及第1軸
print(arr.transpose((1, 0, 2)))
print(arr[0][0][0])
print(arr[0][0][1])
print(arr[0][0][2])
print(arr[1][0][0])
print(arr[1][0][1])
print(arr[1][0][2])
print(arr[0][1][0])
print(arr[0][1][1])
print(arr[0][1][2])
print(arr[1][1][0])
print(arr[1][1][1])
print(arr[1][1][2])

'''
使用 swapaxes 進行軸對換
'''
print(arr)
print(arr[0][0][0])
print(arr[0][0][1])
print(arr[0][0][2])

print(arr[0][1][0])
print(arr[0][1][1])
print(arr[0][1][2])

print(arr[1][0][0])
print(arr[1][0][1])
print(arr[1][0][2])

print(arr[1][1][0])
print(arr[1][1][1])
print(arr[1][1][2])
print(arr.shape)

print(arr)
print(arr[0][0][0])
print(arr[0][1][0])

print(arr[0][0][1])
print(arr[0][1][1])

print(arr[0][0][2])
print(arr[0][1][2])

print(arr[1][0][0])
print(arr[1][1][0])

print(arr[1][0][1])
print(arr[1][1][1])

print(arr[1][0][2])
print(arr[1][1][2])
arr = arr.swapaxes(1, 2)  # 就是将第三个维度和第二个维度交换
print(arr)