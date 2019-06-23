import pandas as pd

obj = pd.Series([4, 7, -5, 3])
print(obj)
print(obj.index)
print(obj.values)

obj = pd.Series([4, 7, -5, 3],index=['d','c','a','g'])
print(obj)
print(obj.index)
print(obj.values)


print(obj['a'])

obj['a'] = 100
print(obj['a'])
print(obj[['a','c']])

#運算
print(obj[obj > 50])
print(obj * 2)
