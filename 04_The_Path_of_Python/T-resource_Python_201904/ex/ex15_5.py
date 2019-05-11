# ex15_5.py
def division(x, y):
    try:                        # try - except指令
        x = int(x)
        y = int(y)
        return x / y
    except Exception:          # 除法的資料型態不符
        print("資料輸入錯誤")
while True:
    op1 = input("請輸入第1個數字 : ")
    op2 = input("請輸入第2個數字 : ")
    print(division(op1, op2))
    con = input("是否繼續(y/n), 輸入n或N代表不繼續 ? ")
    if con == "N" or con == "n":
        break








