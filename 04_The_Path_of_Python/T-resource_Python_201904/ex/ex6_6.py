# ex6_6.py
sc = [['洪錦魁', 80, 95, 88, 0, 0],
      ['洪冰儒', 98, 97, 96, 0, 0],
      ['洪雨星', 91, 93, 95, 0, 0],
      ['洪冰雨', 92, 94, 90, 0, 0],
      ['洪星宇', 92, 97, 90, 0, 0],
     ]      
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
sc[2][4] = sum(sc[2][1:4])
sc[3][4] = sum(sc[3][1:4])
sc[4][4] = sum(sc[4][1:4])
sc[0][5] = round((sc[0][4] / 3), 1)
sc[1][5] = round((sc[1][4] / 3), 1)
sc[2][5] = round((sc[2][4] / 3), 1)
sc[3][5] = round((sc[3][4] / 3), 1) 
sc[4][5] = round((sc[4][4] / 3), 1) 
print(sc[0])   
print(sc[1])
print(sc[2])
print(sc[3])
print(sc[4])











