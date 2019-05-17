scores = [33, 22, 41, 25, 39, 43, 27, 38, 40]
games = 0
for score in scores:
    if score < 30:
        continue
    games += 1
print("有%d場比賽分數是大於等於30"%games)

players = [
    ['James', 202],
    ['Curry', 193],
    ['Durant', 205],
    ['Jordan', 199],
    ['David', 211],    
    ]
for player in players:
    if player[1]<200:
        continue
    print(player[0] +  ' : '+ str(player[1]))

    