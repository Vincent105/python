for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print('%dx%d=%-3d' % (i,j,result), end="")
    print()            