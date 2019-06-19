import numpy as np

arr = np.arange(10)
arr2 = np.arange(20)
np.save('A03_Machine_learning\\E01_python_for_data_analysis\\04_NumPy\\some_numpy', arr)

print(np.load('A03_Machine_learning\\E01_python_for_data_analysis\\04_NumPy\\some_numpy.npy'))

np.savez('A03_Machine_learning\\E01_python_for_data_analysis\\04_NumPy\\array_archive.npz', a=arr, b=arr2)
arch = np.load('A03_Machine_learning\\E01_python_for_data_analysis\\04_NumPy\\array_archive.npz')    
print(arch['a'])
print(arch['b'])    

#可將數據進行壓縮
np.savez_compressed('A03_Machine_learning\\E01_python_for_data_analysis\\04_NumPy\\array_archive.npz', a=arr, b=arr2)   
arch2 = np.load('A03_Machine_learning\\E01_python_for_data_analysis\\04_NumPy\\array_archive.npz')    
print(arch['a'])
print(arch['b'])