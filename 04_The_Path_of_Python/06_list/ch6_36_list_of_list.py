james = [['Lebron James', 'SF', '12/30/84'], 23, 19, 22, 31, 18]
game =len(james)    #先得到list中元素的總數量

total_scores = sum(james[1:game])
max_scores = max(james[1:game])
min_scores = min(james[1:game])
i = james.index(max_scores)
j = james.index(min_scores)

name, position, born = james[0]

print('總得分為:%d'%total_scores)
print('總高得分:%d 場次:%d'%(max_scores,i))
print('總低得分:%d 場次:%d'%(min_scores,j))
print('姓名:',name)
print('位置:',position)
print('生日:',born)