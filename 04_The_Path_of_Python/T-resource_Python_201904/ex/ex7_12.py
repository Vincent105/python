# ex7_12.py
title = "9 * 9 Multiplication Table"
print("%s" % title.center(40))
for i in range(1,10):
    print("%4d" % i, end='')
print()                                 # 跳新行列印
for i in range(40):
    print("=", end='')                  # 列印分隔符號
print()                                 # 跳新行列印
for i in range(1, 10):
    print(i, '|', end='')
    for j in range(1, 10):
        print("%4d" % (i*j), end='')    # 列印乘法值
    print()                             # 跳新行列印




    
   




