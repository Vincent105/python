# decorator 1
def upper(func):
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        print("函數名稱", func.__name__)
        print("函數參數", args)
        return newresult
    return newFunc


@upper
def greeting(string):
    return string


print(greeting('hello'))
# mygreeting = upper(greeting)
# print(mygreeting('hello'))

# decorator 2


def errcheck(func):
    def newFunc(*args):
        if args[1] != 0:
            result = func(*args)
        else:
            result = "除數不可為0"
        print('函數名稱:', func.__name__)
        print('函數參數:', args)
        print('執行結果:', result)
    return newFunc


@errcheck
def mydiv(x, y):
    return x/y


print(mydiv(6, 2))
print(mydiv(6, 0))


# decorator 3
def upper(func):
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        return newresult
    return newFunc


def bold(func):
    def wrapper(args):
        return 'bold' + func(args) + 'bold'
    return wrapper

@bold
@upper
def greeting(string):
    return string

print(greeting('Hello iPhone'))

# decorator 4
def upper(func):
    def newFunc(args):
        oldresult = func(args)
        newresult = oldresult.upper()
        return newresult
    return newFunc


def bold(func):
    def wrapper(args):
        return 'bold' + func(args) + 'bold'
    return wrapper

@upper
@bold
def greeting(string):
    return string

print(greeting('Hello iPhone'))
