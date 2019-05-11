# ex23_7.py
import numpy as np
import matplotlib.pyplot as plt

d1 = np.random.randint(1,6+1,10000)
d2 = np.random.randint(1,6+1,10000)
d3 = np.random.randint(1,6+1,10000)
dsums = d1 + d2 + d3

plt.hist(dsums, 16)
plt.show()









