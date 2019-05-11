# ex7_3.py
money = eval(input("請輸入存款本金 : "))              
rate = eval(input("請輸入年利率   : "))
n = eval(input("請輸入多少年   : "))
for i in range(n):
    money = money * (1 + rate)
    print("第 %d 年本金和 : %d" % ((i+1),money))




