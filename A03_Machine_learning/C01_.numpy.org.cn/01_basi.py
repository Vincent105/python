import numpy as np
my_arrary = np.array([1, 2, 3, 4, 5])
print(my_arrary)

print(my_arrary.shape)  # 包含五個元素的陣列
print(my_arrary[0])
print(my_arrary[1])
my_arrary[0] = -1
print(my_arrary)

# np.zeros  建立長度五 但所有元素為0的陣列
my_zero_array = np.zeros((5))
print(my_zero_array)

# np.zeros  建立2維 長度3 但所有元素為0的陣列
my_2d_array = np.zeros((2, 3))
print(my_2d_array)

# np.ones  建立長度五 但所有元素為1的陣列
my_one_array = np.ones((5))
print(my_one_array)

# np.random.random  建立長度五 但所有元素random的陣列
my_random_array = np.random.random((5))
print(my_random_array)

my_arrary = np.array([[4, 5], [6, 1]])
print(my_arrary[0])
print(my_arrary[0][1])
print(my_arrary.shape)

#从多维NumPy数组中提取一行
my_array_column_2 = my_arrary[:, 1]
print(my_array_column_2)
