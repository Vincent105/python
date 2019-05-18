sc = [
    [1,'Vincent',80,95,88,0,0,0],
    [2,'esther',98,97,96,0,0,0],
    [3,'john',91,70,88,0,0,0],
    [4,'jerry',100,95,90,0,0,0],
    [5,'tim',88,91,70,0,0,0],
]

print('填入總分與平均')
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])
    sc[i][6] = round(sum(sc[i][2:5])/3, 1)
    print(sc[i])

print("填入名次")
sc.sort(key=lambda x:x[5],reverse=True)    
for i in range(len(sc)):
    sc[i][7] = i + 1
    print(sc[i])

print("依座位排序")
sc.sort(key=lambda x:x[0])

for i in range(len(sc)):    
    print(sc[i])

