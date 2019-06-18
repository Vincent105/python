import numpy as np

arr = np.arange(10)
print(arr)

# 返回陣列的平方根
print('第一次取得陣列的平方根',np.sqrt(arr))
# print('第二次取得陣列的平方根',np.sqrt(arr, arr))

# 返回陣列的指數
print(np.exp(arr))

x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print(y)

'''
# np.maximum() np.minimum
'''
a = np.maximum(x, y)
print('兩陣列對應的元素當中取得最大值:', a)

b = np.minimum(x, y)
print('兩陣列對應的元素當中取得最小值:', b)

arr = np.random.randn(7)*5
print(arr)

'''
# np.modf() 拆分 浮點數 陣列
'''
remainder, whole_part = np.modf(arr)
print(remainder)
print(whole_part)



