import numpy as np

names = np.array(
    ['Bob', 'vincent', 'esther', 'john', 'Joe', 'Joe', 'Bob']
)
data = np.random.randn(7, 4)

print(names)
print(data)

print(names == 'Bob')
# 布林值陣列可使用於陣列索引 布尔型数组的长度必须跟被索引的轴长度一致。
print(data[names == 'Bob'])

print(data[names == 'Bob', :2])
print(data[names == 'Bob', 3])

'''
可以使用不等于符号（!=）：  使用&（和）、|（或）之类的布尔算术运算符
'''
print(names != 'Bob')
print(data[names != 'Bob'])

mask = (names == 'Bob') | (names == 'Joe')
print(mask)
print(data[mask])

'''
通过布尔型数组设置值
'''
data[data < 0] = 0
print(data)

data[names != 'Joe'] = 7
print(data)