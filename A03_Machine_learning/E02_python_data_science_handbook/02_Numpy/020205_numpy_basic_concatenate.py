import numpy as np

print("一緯陣列拼接")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.array([7, 8, 9])

set1 = np.concatenate([x, y])
print(set1)

set2 = np.concatenate([x, y, z])
print(set2)

print("二緯陣列拼接")
grid = np.array([[1, 2, 3], [4, 5, 6]])
print(grid)

con1 = np.concatenate([grid, grid], axis=0)
print(con1)
con2 = np.concatenate([grid, grid], axis=1)
print(con2)

print("np.vstack（垂直拼接）")
x = np.array([1, 2, 3])
grid = np.array([[4, 5, 6], [99, 98, 97]])
print(np.vstack([x, grid]))

print("np.hstack（水平拼接）")
y = np.array([[100], [400]])
print(np.hstack([y, grid]))
