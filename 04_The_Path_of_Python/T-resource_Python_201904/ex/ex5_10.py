# ex5_10.py
a, b, c = eval(input("請輸入一元二次方程式的係數 : "))
flag = b**2 - 4*a*c
if flag > 0:
    print("有2個根")
    r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
    print("r1 = %6.4f,    r2 = %6.4f" % (r1, r2))
elif flag == 0:
    print("有1個根")
    r1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    print("r1 = %6.4f" % r1)
else:
    print("沒有實數根")









    


    







