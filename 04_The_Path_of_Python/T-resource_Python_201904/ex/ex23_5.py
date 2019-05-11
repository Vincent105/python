# ex23_5.py
import numpy as np

gcdA = np.gcd(88, 108)
print("[88 108]最大公因數 ", gcdA)

gcdB = np.gcd.reduce([25, 35, 45, 55])
print("[25 35 45 55]最大公因數 ", gcdB)

lcmA = np.lcm(88, 108)
print("[88 108]最小公倍數 ", lcmA)

lcmB = np.lcm.reduce([25, 35, 45, 55])
print("[25 35 45 55]最小公倍數 ", lcmB)




















