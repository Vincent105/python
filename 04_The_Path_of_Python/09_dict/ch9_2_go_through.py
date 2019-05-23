players = {'Vincent':'A-team', 
           'Esther':'B-team',
           'John':'A-team', 
           'Frank':'C-team', 
           'Jerry':'B-team'
}
for name, team in players.items():
    print(name + ' is in ' + team)

for name in players.keys():
    print(name)    

for team in players.values():
    print(team)    

for team in sorted(players.values()):
    print(team)    

noodles = {
    '牛肉麵':100,
    '陽春麵':50,
    '肉絲麵':80,
    '大滷麵':90,
    '麻醬麵':85
}

noodlists = sorted(noodles.items(),key=lambda item:item[1], reverse=True)
print(noodlists)

print(max(noodles.values()))
print(min(noodles.values()))