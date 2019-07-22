import pandas as pd
import numpy as np

print("建立案例")
obj = pd.Series(['4.5', '7.2', '-5.3', '3.6'], index=['d', 'b', 'a', 'c'])
print(obj)

print("使用reindex根據新的索引進行重新排列，如果沒有索引值就引入缺省值")
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

print("对于时间序列之有序数据，重新索引时可能需要做插值处理。method选项使用ffill可以实现前向值填充：")
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)
obj3 = obj3.reindex(range(6), method='ffill')
print(obj3)

print("reindex可以修改（行）索引和列。只传递一个序列时，会重新索引结果的行：")
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=[
                     'a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
print(frame)

frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)

print("列可以用columns关键字重新索引：")
states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))
