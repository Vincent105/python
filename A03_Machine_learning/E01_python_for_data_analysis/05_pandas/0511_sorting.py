import pandas as pd
import numpy as np

print("Series:對索引排序")
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj.sort_index())
