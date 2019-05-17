#list the number of the team
players = ['Vincent', 'Esther', 'Obama', 'Lin' ,'Kevin']

n = int(input("請輸入球員數量:"))

if n > len(players):n == len(players)

index = 0
for player in players:
    if index == n:
        break
    print(player, end=' ') 
    index += 1



        