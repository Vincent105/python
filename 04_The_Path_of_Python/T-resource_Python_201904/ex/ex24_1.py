# ex24_1.py
import numpy as np
from scipy import linalg

# 定義陣列
coeff = np.array([[1,3,5],[2,5,1],[2,3,8]])
deps = np.array([20,12,6])

# 求解
ans = linalg.solve(coeff, deps)

print(ans)









