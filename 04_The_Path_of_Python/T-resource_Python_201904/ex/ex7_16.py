# ex7_16.py
x1 = eval(input("請輸入數值 1 : "))
x2 = eval(input("請輸入數值 2 : "))

gcd = 1
n = 2
while n <= x1 and n <= x2:
    if x1 % n == 0 and x2 % n == 0:
        gcd = n
    n += 1

print("%d 和 %d 的最大公約數是 : %d" % (x1, x2, gcd))







    
   




