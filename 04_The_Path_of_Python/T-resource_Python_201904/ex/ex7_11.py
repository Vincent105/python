# ex7_11.py
n = 10
for i in range(1,n):
    for j in range(n-i,0,-1):
        print(" ", end='')
    
    for k in range(i,0,-1):
        print(k, end='')
    print()




