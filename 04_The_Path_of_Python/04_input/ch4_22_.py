import math

s = eval(input('請輸入五角形邊長：'))
area = (5 * s ** 2) / (4 * math.tan(math.pi / 5 ))

print("area=" ,area)