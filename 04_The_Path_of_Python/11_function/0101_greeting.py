def greeting(name):
    '''傳遞一個參數'''
    print(name + "祝福你")


def subtract(x1, x2):
    '''傳遞兩個參數'''
    result = x1 - x2
    print(result)


def interest(interest_type, subject):
    '''顯示興趣與主題'''
    print('我的興趣是' + interest_type)
    print('在' + interest_type + '中我最喜歡' + subject)
    print()


greeting('Vincent')

interest('旅遊', '日本')

print("本程式可做相減運算")
a = int(input("請輸入a:"))
b = int(input("請輸入b:"))
print("a-b=", end='')
subtract(a, b)
