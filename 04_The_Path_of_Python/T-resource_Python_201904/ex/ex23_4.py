# ex23_4.py
import numpy as np

coeff = np.array([[6,5],[9,2]])
deps = np.array([100,50])
ans = np.linalg.solve(coeff, deps)
print("x = ", ans[0])
print("y = ", ans[1])
















