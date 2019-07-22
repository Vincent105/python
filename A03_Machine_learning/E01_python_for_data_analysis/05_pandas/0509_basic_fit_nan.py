# 在算术方法中填充＃
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))

print("使用np.nan 將4x5矩陣1b轉為NaN")
df2.loc[1, 'b'] = np.nan
print(df2)

print("相加时，没有重叠的位置就会产生NA值：")
print(df1 + df2)

print("使用df1的add方法，传入df2以及一个fill_value参数： 避免nan值")
print(df1.add(df2, fill_value=0))
print(df1)
print("这两个语句是等价的：")
print(1 / df1)
print("使用r針對參數反轉,这两个语句是等价的：")
print(df1.rdiv(1))

print(df1.radd(1))
print(df1.rsub(1))
print(df1.rmul(1))
print("重新索引时，也可以指定一个填充值：")
print(df1.reindex(columns=df2.columns, fill_value=0))