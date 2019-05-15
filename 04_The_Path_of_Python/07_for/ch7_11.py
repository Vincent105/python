money = 50000
rate = 0.015
n = 5

for i in range(5):
    money *=( 1 + rate)
    print("第 %d 年本金和 = %d"%((i+1),(money)))

n = int(input("請輸入n值："))
sum = 0
for num in range(1,n+1):
    sum += num
print("合計：",sum)    
