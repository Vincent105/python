import pandas as pd
import numpy as np

obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)
print(index[1:])

print("Index对象是不可变的，因此用户不能对其进行修改：")
# index[1] = 'd'

print("不可变可以使Index对象在多个数据结构之间安全共享：")
labels = pd.Index(np.arange(3))

print(labels)

obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2)
print(obj2.index is labels)


print("Index的功能类似一个固定大小的集合：")
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame_3 = pd.DataFrame(pop)
frame_3.index.name = 'year'
frame_3.columns.name = 'state'
print(frame_3)
print(frame_3.columns)
print('Ohio' in frame_3.columns)
print(frame_3.index)
print(2000 in frame_3.index)

print("与python的集合不同，pandas的Index可以包含重复的标签：")
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
print(dup_labels)



 