import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn; seaborn.set() 


L = np.random.random(10)
print(sum(L))
print(np.sum(L))

big_arrary = np.random.rand(1000)
print(min(big_arrary))
print(max(big_arrary))

print(np.min(big_arrary))
print(np.max(big_arrary))
print(big_arrary.sum(), big_arrary.min(), big_arrary.max())

print('''axis 关键字指定的是数组将会被折叠的维度， 而不是将要返回的维度。 
因此指定axis=0 意味着第一个轴将要被折叠——对于二维数组， 这意味着每一列的值都将被聚合。''')

M = np.random.random((3, 4))
print(M)
print(M.sum())
print(np.sum(M))
print(M.min(axis=0))
print(M.min(axis=1))
print(M.max(axis=0))
print(M.max(axis=1))

print('建立一組計算身高的範例')
data = pd.read_csv('A03_Machine_learning\\E02_python_data_science_handbook\\02_Numpy\\president_heights.csv')
heights = np.array(data['height(cm)'])

print(data)
print(heights)
print(heights.mean())
print(heights.std())
print(heights.min())
print(heights.max())
print(np.percentile(heights,25))
print(np.percentile(heights,50))
print(np.median(heights))
print(np.percentile(heights,75))

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')
plt.show()

