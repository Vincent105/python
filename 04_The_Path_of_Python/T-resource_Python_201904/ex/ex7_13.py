# ex7_13.py
num = 2
prime = []
primeNum = 0
while primeNum < 20:
    if num == 2:                                # 2是質數所以直接輸出
        prime.append(num)
        primeNum += 1
    else:
        for n in range(2, num):                 # 用2 .. num-1當除數測試
            if num % n == 0:                    # 如果整除則不是質數
                break                           # 離開迴圈
        else:                                   # 否則是質數
            primeNum += 1
            prime.append(num)
    num += 1

print(prime)
