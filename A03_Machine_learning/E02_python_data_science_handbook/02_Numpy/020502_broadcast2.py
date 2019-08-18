import numpy as np
import matplotlib.pyplot as plt

print('陣列歸一化')
x = np.random.random((10, 3))
print(x)
'''
xmean = np.mean(x, axis=1)
print(xmean)
xmean = x.mean(1)
print(xmean)
'''
xmean = np.mean(x, axis=0)
print(xmean)
xmean = x.mean(0)
print(xmean)

x_centered = x - xmean
print(x_centered)

print(x_centered.mean(0))

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:,np.newaxis]
print(x)
print(y)
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

plt.imshow(z,origin='lower',extent=[0,5,0,5],cmap='viridis')
plt.colorbar()
plt.show()