def total(data):
    return sum(data)


x = (1, 5, 10)
mylist = [min, max, sum, total]
for f in mylist:
    print(f, f(x))

# 函數可以當作參數傳遞給其他函數


def add(x, y):
    return x+y


def mul(x, y):
    return x*y


def running(func, arg1, arg2):
    return func(arg1, arg2)


result1 = running(add, 10, 5)
print(result1)
result2 = running(add, 10, 5)
print(result2)

# 函數的參數不定量


def mysum(*args):
    return sum(args)


def run_with_multiple_args(func, *args):
    return func(*args)


print(run_with_multiple_args(mysum, 1, 2, 3, 4, 5, 6, 7))