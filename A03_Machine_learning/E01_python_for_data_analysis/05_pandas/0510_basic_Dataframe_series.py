import pandas as pd
import numpy as np

arr = np.arange(12.).reshape((3, 4))
print(arr)

print("計算陣列與某行之差－每一行都會執行此操作，通稱broadcasting…Dataframe與series差不多如是")
print(arr[0])
print(arr - arr[0])

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)),
                     columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]

print(frame)
print(series)
print("broadcasting")
print(frame - series)

print("broadcasting，重新索引 找不到時以NaN顯示")
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(frame - series2)

series3 = frame['d']
print(frame)
print(series3)

print("如果希望匹配行且在列上广播，则必须使用算术运算方法")
print(frame.sub(series3, axis=0))



