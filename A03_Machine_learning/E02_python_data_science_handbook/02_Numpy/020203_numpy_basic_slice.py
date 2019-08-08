import numpy as np

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))

print("x[start:stop:step]")

x = np.arange(10)
print(x)
print(x[:5])
print(x[5:])
print(x[4:7])
print(x[::2])
print(x[1::2])
 
print("所有元素， 逆序的") 
print(x[::-1])
print("# 从索引5开始每隔一个元素逆序")
print(x[5::-2])
 