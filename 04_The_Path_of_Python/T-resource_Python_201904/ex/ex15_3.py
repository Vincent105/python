# ex15_3.py
def division(x, y):
    try:                        # try - except指令
        x = int(x)
        y = int(y)
        return x / y
    except ZeroDivisionError:   # 除數為0時執行
        print("除數不可為0")
    except ValueError:          # 除法的資料型態不符
        print("除法資料型態不符")

op1 = input("請輸入第1個數字 : ")
op2 = input("請輸入第2個數字 : ")
print(division(op1, op2))          





