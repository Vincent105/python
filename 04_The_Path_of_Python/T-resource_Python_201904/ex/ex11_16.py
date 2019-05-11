# ex11_16.py
mylist = [25,18,12,22,31,17,26,19,18,10]

sclist = list(filter(lambda x: (x >= 20), mylist))

# 輸出得分大於或等於20分的串列
print("得分大於或等於20分的串列: ",sclist)

