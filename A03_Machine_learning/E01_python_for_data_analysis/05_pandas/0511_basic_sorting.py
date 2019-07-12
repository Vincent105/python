import pandas as pd
import numpy as np
'''
索引排序
'''
print("Series:索引排序")
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())

print("Datafrmae:索引排序,升冪排序")
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
                     index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
print(frame.sort_index())
print(frame.sort_index(axis=1))
print("Datafrmae:索引排序,降冪排序")
print(frame.sort_index(axis=1, ascending=False))

'''
按值排序
'''
print("Series:按值排序")
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_values())

print("Series:按值排序，任何缺失值默认都会被放到Series的末尾：")
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.sort_values())

print("Datafrmae:使用by選項－根据一个或多个列中的值进行排序。")
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame.sort_values(by='b'))
print("根据多个列进行排序，传入名称的列表即可：")
print(frame.sort_values(by=['a', 'b']))

'''
Rank排序
'''
print("Series:Rank排序 - 通过“为各组分配一个平均排名”")
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())
print(obj.rank(method='average'))
print("根据值在原数据中出现的顺序给出排名：这里，条目0和2没有使用平均排名6.5，它们被设成了6和7，因为数据中标签0位于标签2的前面。")
print(obj.rank(method='first'))
print(obj.rank(method='min'))
print(obj.rank(method='max'))
print(obj.rank(ascending=False))  # 降序排列

print("Datafrmae:Rank排序")
frame = pd.DataFrame({
    'b': [4.3, 7, -3, 2],
    'a': [0, 1, 0, 1],
    'c': [-2, 5, 8, -2.5]
})
print(frame)
print(frame.rank(axis='columns'))
