# ex24_6.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = np.linspace(0,10,11)
y = np.cos(x**2/9)

fLinear = interp1d(x,y)                             # Linear插值函數
fCubic = interp1d(x,y,kind='cubic')                 # Cubic插值函數
xnew = np.linspace(0,10,51)                         # 擴充的x軸數據

plt.plot(x,y,'o',label='data')
plt.plot(xnew,fLinear(xnew),'-',label='linear')     # Linear
plt.plot(xnew,fCubic(xnew),'--',label='cubic')      # Cubic

plt.legend(loc='best')
plt.show()



      














