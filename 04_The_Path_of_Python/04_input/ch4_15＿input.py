print('歡迎進入成績計算系統')
name = input('請輸入姓名：')
eng = input('請輸入英文成績：')
math = input('請輸入數學成績：')

totalScorce = int(eng)+int(math)
print('{0}你的總成績是{1}'.format(name,totalScorce))
print('%s你的總成績是%d'%(name,totalScorce))
