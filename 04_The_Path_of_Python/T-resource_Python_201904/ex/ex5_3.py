# ex5_3.py
r = 20
x, y  = eval(input("請輸入點座標 : "))
dist = (x * x + y * y) ** 0.5   # 計算點與圓中心距離

if dist > r:
    print("點座標(%s,%s)不在圓內部" % (str(x), str(y)))
else:
    print("點座標(%s,%s)在圓內部" % (str(x), str(y)))



