def product_msg(customers):
    str1 = "親愛的: "
    str2 = "本公司將於2020年舉行發表會"
    str3 = "總經理敬上"
    for customer in customers:
        msg = str1 + customer + '\n' + str2 + '\n' + str3
        print(msg, '\n')


members = ['vincent', 'esther', 'john']

product_msg(members)

# 傳遞一般變數與串列變數的區別


def mydata(n):
    print("(2)副程式 id(n)=:", id(n), "\t", n)
    n = 5
    print("(3)副程式 id(n)=:", id(n), "\t", n)


x = 1
print("(1)主程式 id(x)=:", id(x), "\t", x)
mydata(x)
print("(4)主程式 id(x)=:", id(x), "\t", x)


def mydata_list(n):
    print("(2)副程式 id(n)=:", id(n), "\t", n)
    n[0] = 5
    print("(3)副程式 id(n)=:", id(n), "\t", n)


x = [1, 2]
print("(1)主程式 id(x)=:", id(x), "\t", x)
mydata_list(x)
print("(4)主程式 id(x)=:", id(x), "\t", x)
