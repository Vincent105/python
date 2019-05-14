num1, num2, num3, num4, num5 = eval(input("請輸入5個考試成績:"))
sc = [num1, num2, num3, num4, num5]

print("列出分數串列:",sc)
print("列出分數串列:由高分排序至低分:",sorted(sc, reverse=True))
print("列出分數串列:由低分排序至高分:",sorted(sc))
print("列出分數串列:最高分:",max(sc))
print("列出分數串列:最低分:",min(sc))
print("列出分數串列:總分數:",sum(sc))

