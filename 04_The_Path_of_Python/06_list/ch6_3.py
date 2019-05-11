james = [23,19,22,31,18]
game1 = james[0]
game2 = james[1]
print(game1,game2)

#較好的List賦值
game1,game2,game3,game4,game5 = james
print(game1,game2,game3)

#List統計
print('List的最大數值是',max(james[0:5]))
print('List的最小數值是',min(james[0:5]))
print('List的加總數值是',sum(james[0:5]))

#Len
vincent_score = [23, 19, 22, 31, 18]
game_times = len(vincent_score)

print('經過合計 %d 比賽最高得分= '%game_times,max(vincent_score))
print('經過合計 %d 比賽最低得分= '%game_times,min(vincent_score))
print('經過合計 %d 比賽加總得分= '%game_times,sum(vincent_score))

#替換List元素
vincent_score = [23, 19, 22, 31, 18]
print(vincent_score)
vincent_score[0] = 44
print(vincent_score) 