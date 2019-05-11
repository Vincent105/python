# ex11_14.py
def evenfn(x):
    return x if (x % 2 == 0) else None

mylist = [5, 10, 15, 20, 25, 30]
filter_object = filter(evenfn, mylist)     # 傳回filter object

# 輸出偶數串列
print("偶數串列: ",[item for item in filter_object])




