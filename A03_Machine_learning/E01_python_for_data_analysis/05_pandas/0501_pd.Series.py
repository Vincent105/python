import pandas as pd
import numpy as np 

# basic pandas
obj = pd.Series([4, 7, -5, 3])
print(obj)
print(obj.index)
print(obj.values)

# pandas with index
obj = pd.Series([4, 7, -5, 3],index=['d','c','a','g'])
print(obj)
print(obj.index)
print(obj.values)

# with index 
print(obj['a'])

obj['a'] = 100
print(obj['a'])
print(obj[['a','c']])

#運算
print("運算")
print(obj[obj > 50])
print(obj * 2)
print(np.exp(obj))
print('d' in obj)
print('z' in obj)

print("通过字典创建Series")
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

print("有序排列")
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata,index=states)
print(obj4)

# missing判斷
print(pd.isnull(obj4))
print(pd.notnull(obj4))
