print('歡迎使用成績輸入系統')
name = input('請輸入姓名：')
engh = eval(input('請輸入英文成績：'))
math = eval(input('請輸入數學成績：'))

totalScore = engh + math
print('%s你的總成績是:%d'%(name,totalScore))
