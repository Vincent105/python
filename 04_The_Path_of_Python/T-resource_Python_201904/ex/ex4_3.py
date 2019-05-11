# ex4_3.py
f = open("out.txt",mode="w")
print(" 姓名    國文    英文    總分    平均",file=f)
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪冰儒", 98, 90, 188, 188/2),file=f)
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪雨星", 96, 95, 191, 191/2),file=f)
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪冰雨", 92, 88, 180, 180/2),file=f)
print("%3s  %4d    %4d    %4d     %3.1f" % ("洪星宇", 93, 97, 190, 190/2),file=f)
f.close()

