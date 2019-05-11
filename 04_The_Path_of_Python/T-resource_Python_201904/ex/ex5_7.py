# ex5_7.py
today = "星期一"
print("今天是星期日")
days = eval(input("請輸入天數 : "))
day = days % 7
if day == 0:
    print("%d 天後是星期日" % days)           
elif day == 1:    
    print("%d 天後是星期一" % days)
elif day == 2:    
    print("%d 天後是星期二" % days)
elif day == 3:    
    print("%d 天後是星期三" % days)
elif day == 4:    
    print("%d 天後是星期四" % days)
elif day == 5:    
    print("%d 天後是星期五" % days)
else:    
    print("%d 天後是星期六" % days)

