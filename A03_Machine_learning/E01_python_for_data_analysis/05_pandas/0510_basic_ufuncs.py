import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print("取絕對值")
print(np.abs(frame))

print("")

print("将函数应用到由各列或行所形成的一维数组上。DataFrame的apply方法可实现此功能：")


def f(x): return x.max()-x.min()


print(frame.apply(f, axis=0))
print(frame.apply(f, axis='index'))
print(frame.apply(f, axis=1))
print(frame.apply(f, axis='columns'))


def f(x):
    return pd.Series([x.min(), x.max()], index=['min', 'max'])
print(frame.apply(f))

print("元素级的Python函数也是可以用的。假如想得到frame中各个浮点值的格式化字符串，使用applymap：")
format = lambda x: '%.2f'% x
print(frame.applymap(format))
print(frame['e'].map(format))
