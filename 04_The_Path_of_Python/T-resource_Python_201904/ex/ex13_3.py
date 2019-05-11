# ex13_3.py
import random                       # 導入模組random

min, max = 1, 30
ans = random.randint(min, max)      # 隨機數產生答案
count = 0                           # 計算猜測次數
while True:
    num = input("請猜1-30之間數字: ")
    if num == 'Q' or num == 'q':
        break
    yourNum = int(num)
    count += 1
    if yourNum == ans:
        print("恭喜!答對了")
        print("總共猜測 %d 次" % count)
        break
    elif yourNum < ans:
        print("請猜大一些")
    else:
        print("請猜小一些")
        


