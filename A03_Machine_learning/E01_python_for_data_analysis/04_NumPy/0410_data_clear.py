import numpy as np
import matplotlib.pyplot as plt

# np.meshgrid 接受兩個1緯陣列，產生2緯陣列
points = np.arange(-5, 5, 1)
print(points)
xs, ys = np.meshgrid(points, points)
print(ys)

z = np.sqrt(xs**2 + ys**2)
print(z)
'''
透過matplotlib建立可視化二緯陣列
'''
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()


