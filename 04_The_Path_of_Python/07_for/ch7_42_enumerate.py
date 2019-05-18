drinks = ['coffee', 'tea', 'wine']
for drink in enumerate(drinks):             #數值初始化從0開始  
    print(drink)

for count, drink in enumerate(drinks):
    print(count, drink)     

for count, drink in enumerate(drinks,10):   #數值初始化從10開始
    print(count, drink)     

scores = [21,29,18,33,12,17,26,28,15,19]
index = 1
for score in scores:
    if score >= 20:
        print("場次%d得分%d"%( index, score))
    index += 1

for count, score in enumerate(scores,1):
    if score >= 20:
        print("場次%d得分%d"%( count, score))