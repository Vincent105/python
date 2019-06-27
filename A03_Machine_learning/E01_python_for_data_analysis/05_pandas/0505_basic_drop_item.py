import numpy as np
import pandas as pd

print("建一個案例")
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)

print("試著丟棄索引")
new_obj_1 = obj.drop(['d'])
print(new_obj_1)
new_obj_2 = obj.drop(['d', 'c'])
print(new_obj_2)

print("再建一個案例")
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

print("axis 0 使用drop丟棄")
print(data.drop(['Ohio', 'Colorado']))

print("axis 1 透過傳遞axis=1 或 axis='columns'刪除數值")
print(data.drop('two',axis=1))
print(data.drop(['one','four'],axis='columns'))

print("小心使用inplace，它会销毁所有被删除的数据。")
print(obj)
print(obj.drop('c',inplace=True))
print(obj)

