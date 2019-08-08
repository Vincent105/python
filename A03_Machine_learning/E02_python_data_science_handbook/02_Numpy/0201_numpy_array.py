import numpy
import numpy as np

print("Python 中， 类型是动态推断的")
L = list(range(10))
print(L)
print(type(L[0]))

L2 = [str(c) for c in L]
print(L2)
print(type(L2[0]))

L3 = [True, "2", 3.0, 4]
print([type(item) for item in L3])

print("透過Python列表，建立數組:numpy要求必須是同一類型的數據")
N1 = np.array([1, 2, 3, 4, 5])
print(N1)

N2 = np.array([3.1, 2, 3, 4, 5])
print(N2)

print("keyword:dtype")
N3 = np.array([1, 2, 3, 4, 5], dtype=float)
print(N3)

print("创建一个长度为10的数组， 数组的值都是0")
np1 = np.zeros(10, dtype=int)
print(np1)

print("创建一个3×5的浮点型数组， 数组的值都是1")
np2 = np.ones((3, 5), dtype=float)
print(np2)

print("创建一个3×5的浮点型数组， 数组的值都是3.14")
np3 = np.full((3, 5), 3.14)
print(np3)

print("从0开始， 到20结束， 步长为與range()類似")
np4 = np.arange(0, 20, 2)
print(np4)

print("从0开始， 到2结束，平均分配至5個數據")
np5 = np.linspace(0, 2, 5)
print(np5)

print("创建一个3×3的、 在0~1均匀分布的随机数组成的数组")
np6 = np.random.random((3,3))
print(np6)

print("创建一个3×3的、 均值为0、 方差为1的正态分布的随机数数组")
np7 = np.random.normal(0,1,(3,3))
print(np7)

print("创建一个3×3的、由0, 10)区间的随机整型数组")
np8 = np.random.randint(0,10,(3,3))
print(np8)

print("创建一个3×3的单位矩阵")
np9 = np.eye(3)
print(np9)

print("创建一个由3个整型数组成的未初始化的数组")
np10 = np.empty(3)
print(np10)

print("可以用一个字符串参数来指定数据类型：")
np1 = np.zeros(10,dtype='int16')
print(np1)
np1 = np.zeros(10,dtype=np.int)
print(np1)
