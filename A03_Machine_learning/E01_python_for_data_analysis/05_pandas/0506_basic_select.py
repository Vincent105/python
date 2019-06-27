# 索引、选取和过滤

import pandas as pd
import numpy as np

print("建立一個案例")
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)

print("資料選取")
print(obj['d'])
print(obj[1])
print(obj[2:4])
print(obj[['b', 'a', 'd']])
print(obj[[1, 3]])
print(obj[obj < 2])

print("标签的切片运算与普通的Python切片运算不同，其末端是包含的：")
print(obj['a':'c'])

print("用切片可以对Series的相应部分进行设置")
obj['b', 'c'] = 5
print(obj)

print("用一个值或序列对DataFrame进行索引其实就是获取一个或多个列：")
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data['two'])
print(data[['three', 'one']])

print("通过切片或布尔型数组选取数据：")
print(data[:2])
print(data[data['three'] > 5])

print("通过布尔型DataFrame进行索引：")
print(data < 5)
data[data < 5] = 0
print(data)

