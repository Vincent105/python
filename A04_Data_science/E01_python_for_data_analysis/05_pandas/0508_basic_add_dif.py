# 算术运算和数据对齐
import pandas as pd
import numpy as np

s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])

print(s1 + s2)

print("如果DataFrame对象相加，没有共用的列或行标签，结果都会是空：")
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list(
    'bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list(
    'bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1)
print(df2)
print(df1 + df2)

df1 = pd.DataFrame({'A': [1, 2], 'B': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
print(df1)
print(df2)
print(df1 - df2)

# 在算术方法中填充值