print(dir(__builtins__))

n1, n2, n3 = eval(input('請輸入三個數字:<中間用,相隔>'))
average = (n1 + n2 + n3) / 3

print('3個數字平均是%6.2f'% average)


