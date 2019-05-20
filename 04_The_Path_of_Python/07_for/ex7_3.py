money = int(input("請輸入本金金額:"))
rate = float(input("請輸入每年利率:"))
n = int(input("請輸入總共需要貸款幾年:"))

for i in range(n):
    money *= (1 + rate)
    print("第%d年本金和 = %d"%((i + 1), money))
