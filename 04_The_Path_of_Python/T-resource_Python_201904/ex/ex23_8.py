# ex23_8.py
import numpy as np
import matplotlib.pyplot as plt

mean, sigma = 100, 15
s = np.random.normal(mean, sigma, 10000)
bins = 50
plt.hist(s, bins, density=True)
plt.show()









