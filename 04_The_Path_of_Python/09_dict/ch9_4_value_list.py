sports = {
    'Curry':['籃球', '美式足球'],
    'Vincent':['棒球'],
    'Esther':['美式足球', '棒球', '籃球']}

for name, sport_sets in sports.items():
    print('%s 喜歡的運動:'%name)
    for sport in sport_sets:
        print('\t' + sport)

