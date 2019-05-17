answer = 30
guess = 0
while guess != answer:
    guess = int(input("請輸入1～100的數字:"))
    if guess > answer:
        print("請猜測小一點")
    elif guess < answer:
        print("請猜測大一點")        
    else:
        print("恭喜答對")        
