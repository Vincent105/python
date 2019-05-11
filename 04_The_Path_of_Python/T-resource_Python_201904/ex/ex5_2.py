# ex5_2.py
n1, n2, n3 = eval(input("請輸入3個整數值: "))
if n1 < n2:
    n1, n2 = n2, n1
if n2 < n3:
    n2, n3 = n3, n2
if n1 < n2:
    n1, n2 = n2, n1
print("大到小分別是 ", n1, n2, n3)




