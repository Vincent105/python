import numpy as np

# 透過建立空陣列，將運算結果透過out參數存入陣列
x = np.arange(5)
y = np.empty(5)
print(np.multiply(x, 10, out=y))
print(y)

y = np.zeros(10)
np.power(2, x, out=y[::2])
print(y)

print("对 add 通用函数调用 reduce 方法会返回数组中所有元素的和")
x = np.arange(1, 6)
print(x)
print(np.add.reduce(x))
print(np.multiply.reduce(x))
print(np.add.accumulate(x))
print(np.multiply.accumulate(x))

print("外積")
x = np.arange(1, 6)
print(np.multiply.outer(x, x))
