import random

min, max = 1, 10
ans = random.randint(min, max)
while True:
    yourNum = int(input('請輸入1-10之間的數字：'))
    if yourNum == ans:
        print('you guess the right number.')
        break
    elif yourNum < ans:
        print('guess large')      
    elif yourNum > ans:
        print('guess lower')      