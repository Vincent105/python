# ex5_4.py
print("輸入數字判斷程式")
num = eval(input("請輸入任意整數值: "))
if num != 0:            # 正值改為復值,負值改為正值
    x = -int(num)
    print(x)
else:
    print(num)          # 這是0


