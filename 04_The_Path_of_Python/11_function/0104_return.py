def mutifunction(x1, x2):
    add = x1 + x2
    sub = x1 - x2
    mul = x1 * x2
    div = x1 / x2
    return add, sub, mul, div


x1 = x2 = 10
addresult, subresult, mulresult, divresult = mutifunction(x1, x2)
print(addresult)
print(subresult)
print(mulresult)
print(divresult)

def guest_info(firstname, lastname, gender, middlename=''):
    ''''''
    if gender == "M":
        welcome = "Welcome " + lastname + middlename + firstname + "先生歡迎"
    else:
        welcome = "Welcome " + lastname + middlename + firstname + "小姐歡迎"
    return welcome


info1 = guest_info("宗", "洪", "M")
info2 = guest_info("宗", "王", "F", "星")
print(info1)
print(info2)

def subtract(x1, x2):
    '''減法設計'''
    result = x1 - x2
    return result


def addition(x1, x2):
    '''加法設計'''
    return x1 + x2


print("請選擇運算方式")
print("1:減法")
print("2:加法")
option = int(input("請輸入1或者2選擇運算模式:"))
a = int(input('請輸入a ='))
b = int(input('請輸入b ='))

if option == 1:
    print("a-b=", subtract(a, b))
elif option == 2:
    print("a+b=", addition(a, b))
else:
    print("選擇模式錯誤")
