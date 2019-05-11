sc = [['vicent',80,99,80,0],
      ['esther',70,100,85,0]
    ]

print(sc[0][0:4])
print(sc[1][0:4])

sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])

print(sc[0][4])
print(sc[1][4])
