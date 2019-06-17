import numpy as np

arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr1.dtype)
print(arr2.dtype)

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)

# 透過astype轉換陣列型別
float_arr = arr.astype(np.float64)
print(float_arr.dtype)

arr_a = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr_a = arr_a.astype(np.int64)
print(arr_a)

arr_b = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr_b = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1], dtype=np.int64)
print(arr_b)

# 注意：使用numpy.string_类型时，一定要小心，因为NumPy的字符串数据大小固定的，截取时，不会发出警告。pandas提供了更多非数值数据的便利的处理方法。
numeric_string = np.array(['1.25', '-9.6', '42'],
                          dtype=np.str)  # 如果都是數值可正常從str 轉換為 float
numeric_string_1 = numeric_string.astype(np.float)
print(numeric_string_1)

# 轉型態的另一個方法
int_arrary = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44], dtype=np.float64)
int_arrary = int_arrary.astype(calibers.dtype)
print(int_arrary.dtype)

empty_unit32 = np.empty(8, dtype='u4')
print(empty_unit32)
