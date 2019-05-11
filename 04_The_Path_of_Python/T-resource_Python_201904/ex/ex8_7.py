# ex8_7.py
# 計算平均值
vals = (1100,652,946,821,955,1024,1155)
mean = sum(vals) / len(vals)
print("平均值 : ", mean)

# 計算變異數
var = 0
for v in vals:
    var += ((v - mean)**2)
var = var / (len(vals)-1)
print("變異數 : ", var)

# 計算標準差
dev = 0
for v in vals:
    dev += ((v - mean)**2)
dev = (dev / (len(vals)-1))**0.5
print("標準差 : ", dev)




