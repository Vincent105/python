soldier0 = {'tag':'red', 'score':3, 'speed':'low'}
soldier1 = {'tag':'blue', 'score':5, 'speed':'medium'}
soldier2 = {'tag':'green', 'score':10, 'speed':'fast'}

armys = [soldier0, soldier1, soldier2]
for army in armys:
    print(army)

armys = []
for soldier_number in range(50):
    soldier_number = {'tag':'red', 'score':3, 'speed':'low'}
    armys.append(soldier_number)

for soldier in armys[:]:
    print(soldier)

print(len(armys))    

for soldier in armys[21:40]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'blue'
        soldier['score'] = 5
        soldier['speed'] = 'medium'

for soldier in armys[:]:
    print(soldier)

