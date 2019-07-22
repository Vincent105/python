import numpy as np

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# 透過cond選取xarr 或 yarr的一般條件式寫法
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print(result)

# 透過np.where的簡潔撰寫方式
result = np.where(cond, xarr, yarr)
print(result)

# 進一步解釋 np.where
arr = np.random.randn(4, 4)
print(arr)
print(arr > 0)

result = np.where(arr > 0, 2, -2)
print(result)

result = np.where(arr > 0, 2, arr)  # set only positive values to 2
print(result)
