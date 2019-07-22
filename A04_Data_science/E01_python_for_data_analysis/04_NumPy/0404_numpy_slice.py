import numpy as np

arr = np.arange(10)
print(arr)

print(arr[5])

print(arr[5:8])

arr[5:8] = 12
print(arr)
# 将一个标量值赋值给一个切片时（如arr[5:8]=12），该值会自动传播（也就说后面将会讲到的“广播”）到整个选区。
# 跟列表最重要的区别在于，数组切片是原始数组的视图。这意味着数据不会被复制，视图上的任何修改都会直接反映到源数组上。
arr_slice = arr[5:8]
print(arr_slice)
arr_slice[1] = 12345
print(arr_slice)
print(arr)

arr_slice[:] = 24
print(arr)

# 透過 .copy() 得到切片副本
arr_copy = arr[5:8].copy()
arr_copy[1] = 999
print(arr_copy)
print(arr)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])
print(arr2d.shape)

# 下列兩個方式 等價
print(arr2d[0][2])
print(arr2d[0, 2])

# 2×2×3数组arr3d
arr3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print(arr3d.shape)
print(arr3d[0])

old_values = arr3d[0].copy()

arr3d[0] = 42
print(arr3d)
arr3d[0] = old_values
print(arr3d)
print(arr3d[1][0])

#兩部索引
x = arr3d[1]
print(x)

print(x[0])