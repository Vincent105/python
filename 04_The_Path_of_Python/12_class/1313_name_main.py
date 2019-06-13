# 判定是否為自執行或者被其他程式叫用
def myFun():
    print("__name__ == __main__")


if __name__ == "__main__":
    myFun()
