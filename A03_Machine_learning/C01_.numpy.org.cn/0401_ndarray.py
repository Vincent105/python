import numpy as np

#np.arange == list(range())
my_arr = np.arange(100)  # 陣列
print(my_arr)

my_list = list(range(100))  # 等價的list列表
print(my_list)

# 使用randn產生陣列，進行數學運算
data = np.random.randn(2, 3)
print(data)

result_1 = data * 10
print(result_1)

result_2 = data + data
print(result_2)

print(data.shape)  # 每個陣列都有一個表示各緯度大小的元祖(shape)
print(data.dtype)

# 建立ndarray，並計算緯度數、元素數量、數據型別
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.dtype)

data2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
arr2 = np.array(data2)
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr2.dtype)

# np.zeros np.ones np.arrange
a = np.zeros(10)
print(a)
b = np.ones((2,10))
print(b)
c = np.arange(15)    #range 的陣列版本
print(c)

