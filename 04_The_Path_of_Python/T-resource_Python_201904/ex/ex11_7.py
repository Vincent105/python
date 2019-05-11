# ex11_7.py
def CtoF(c):
    f = (9.0/5.0) * c + 32
    return f
def FtoC(f):
    c = (5.0/9.0) * (f - 32)
    return c

cel = 21
fra = 70

print("攝氏溫度\t華氏溫度\t|\t華氏溫度\t攝氏溫度")
print("=================================================================")
for i in range(10):
    print("  %3d\t\t%6.2f\t\t|\t  %3d\t\t%6.2f" % (cel,CtoF(cel),fra,FtoC(fra)))
    cel += 1
    fra += 5





