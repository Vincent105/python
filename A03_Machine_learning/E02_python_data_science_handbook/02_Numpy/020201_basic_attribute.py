import numpy as np 

'''
NumPy数组的属性
'''
np.random.seed(0)
x1 = np.random.randint(10,size=6)
x2 = np.random.randint(10,size=(3,4))
x3 = np.random.randint(10,size=(3,4,5))

print("一緯陣列")
print(x1)
print("二緯陣列")
print(x2)
print("三緯陣列")
print(x3)

print("x3 ndim-陣列的緯度：",x3.ndim)
print("x3 shape-陣列的大小：",x3.shape)
print("x3 size-陣列的總數：",x3.size)
print("dtype-陣列的數據類型：",x3.dtype)
print("itemsize-陣列每個元素占用的字元大小：",x3.itemsize,"bytes")
print("nbytes-陣列合計占用的字元大小：",x3.nbytes,"bytes")


