# 用loc和iloc进行选取

import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data.loc['Colorado', ['two', 'three']])

print(data.iloc[2, [3, 0, 1]])
print(data.iloc[2])
print(data.iloc[[2, 1], [3, 0, 1]])

# loc和iloc索引函数也适用于一个标签或多个标签的切片：
print(data.loc[:'Utah', 'two'])
print(data.iloc[:, :3][data.three > 5])