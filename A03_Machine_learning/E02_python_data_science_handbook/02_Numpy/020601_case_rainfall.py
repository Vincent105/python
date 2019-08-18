import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
seaborn.set()

rainfall = pd.read_csv(
    'A03_Machine_learning\\E02_python_data_science_handbook\\02_Numpy\\Seattle2014.csv')['PRCP'].values
inches = rainfall / 254
print(inches.shape)
plt.hist(inches, 40);
plt.show()



