import time
import random

print('計算1970年1月1日00:00:00至今秒數=', time.time())


# time.asctime()    列出目前系統時間
print(time.asctime())

localtime = time.localtime()
print(localtime[0])
print(localtime[1])
print(localtime[2])
print(localtime[3])
print(localtime[4])
print(localtime[5])
print(localtime[6])
print(localtime[7])
print(localtime[8])


# time.sleep()
fruits = ['apple', 'mango', 'banana']
for fruit in fruits:
    print(fruit)
    time.sleep(1)

# time.time()
min, max = 1, 10
ans = random.randint(min, max)

yournum = int(input('請輸入1-10之間的數字：'))
starttime = int(time.time())
while True:
    if yournum == ans:
        print('恭喜')
        endtime = int(time.time())
        print('合計花費', endtime - starttime, '秒')
        break
    elif yournum < ans:
        print('要猜大一點')
    else:
        print('要猜小一點')
    yournum = int(input('請輸入1-10之間的數字：'))
