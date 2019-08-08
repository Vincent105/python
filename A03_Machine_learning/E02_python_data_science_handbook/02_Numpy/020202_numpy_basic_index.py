import numpy as np 

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10,size=(3,4))
x3 = np.random.randint(10,size=(3,4,5))

print(x1)
print("通过中括号指定索引获取第 i 个值（从 0 开始计数）")
print(x1[0])
print(x1[4])

print("末尾索引， 负值索引")
print(x1[-1])

print("多维数组中， 可以用逗号分隔的索引元组获取元素")
print(x2)
print(x2[0,0])
print(x2[2,0])

print("透過索引修改元素")
x2[2,0] = 12 
print(x2)
print("NumPy 数组是固定类型的。 这意味着当你试图将一个浮点值插入一个整型数组时， 浮点值会被截短成整型。")
x2[2,1] = 3.147
print(x2)