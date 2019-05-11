# ex24_4.py
from scipy.optimize import root
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return (a*x**2 + b*x)

a = 1
b = 7
r1 = root(f,0)          # 初始迭代值0
print(r1.x)
r2 = root(f,-5)         # 初始迭代值-5
print(r2.x)

x = np.linspace(-10, 10, 100)
y = a*x**2 + b*x
plt.plot(r1.x, f(r1.x), 'o')
plt.plot(r2.x, f(r2.x), 'o')
plt.plot(x, y, '-')
plt.show()










