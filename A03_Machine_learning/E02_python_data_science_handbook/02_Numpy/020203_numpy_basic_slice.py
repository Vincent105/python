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
print(x[5::-2], "从索引5开始每隔一个元素逆序")

print(x2)
print(x2[:2, :3])
print(x2[:3, :2])
print(x2[:3, ::2], "每隔一列")
print(x2[::-1, ::-1])

print("獲取陣列的行列")
print(x2[:, 0])
print(x2[0, :], '=', x2[0])

print("陣列切片為view，並非copy")
print(x2)
x2_sub = x2[:2, :2]
print(x2_sub)
x2_sub[0, 0] = 99
print(x2_sub)
print(x2)

print("透過copy()產生副本")
x2_sub = x2[:2, :2].copy()
x2_sub[0, 0] = 999
print(x2)
print(x2_sub)