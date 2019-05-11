# ex24_3.py
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.integrate import trapz
import numpy as np

x = np.linspace(-3,3,100)
plt.plot(x, st.norm.pdf(x,loc=0, scale=1.5), 'r-')

xs = np.linspace(-1,1,100)
p = trapz(st.norm.pdf(xs, loc=0, scale=1.5), xs)
print("落在-1與1之件的機率是 %4.2f" % (100*p) + "%")
plt.fill_between(xs, st.norm.pdf(xs,loc=0,scale=1.5), color="yellow")

plt.show()











