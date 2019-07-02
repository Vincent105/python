fn = 'E:\\python\\04_The_Path_of_Python\\14_write_read\\ch14_15.txt'

file_obj = open(fn, encoding="utf-8")
data = file_obj.read()
file_obj.close()
print(data.rstrip())

print("Python常用讀取法")
with open(fn, encoding="utf-8") as file_obj:
    data = file_obj.read()
    print(data.rstrip())

print("逐行讀取方式一")
with open(fn, mode='r', encoding="utf-8") as file_obj:
    for line in file_obj:
        print(line.rstrip(), end='-')

print("逐行讀取方式二")
with open(fn, encoding="utf-8") as file_obj:
    obj_list = file_obj.readlines()
    print(obj_list)

print("逐行讀取方式二，將list轉換")
for line in obj_list:
    print(line.rstrip())

print("====數據組合====")
with open(fn, encoding="utf-8") as file_obj:
    obj_list = file_obj.readlines()

str_obj = ''
for line in obj_list:
    str_obj += line.rstrip()
print(str_obj)

print("====字串替換====")
with open(fn, encoding="utf-8") as file_obj:
    data = file_obj.read()
    newdata = data.replace("測試", "實際")
    print(newdata.rstrip())

print("====數據搜尋====")
with open(fn, encoding="utf-8") as file_obj:
    obj_list = file_obj.readlines()

str_obj = ''
for line in obj_list:
    str_obj += line.rstrip()

finstr = input("請輸入查詢的字串：")
if finstr in str_obj:
    print("搜尋的字串%s存在%s當中" % (finstr, fn))
else:
    print("搜尋的字串%s不存在%s當中" % (finstr, fn))

print("====數據搜尋(使用find()方法)====")
with open(fn, encoding="utf-8") as file_obj:
    obj_list = file_obj.readlines()

str_obj = ''
for line in obj_list:
    str_obj += line.rstrip()

findstr = input("請輸入查詢的字串：")
index = str_obj.find(findstr)
if index >= 0:
    print("搜尋的字串%s存在%s當中" % (findstr, fn))
    print("搜尋的字串在%s的位置" % index)
else:
    print("搜尋的字串%s不存在%s當中" % (findstr, fn))

print("====數據搜尋(使用rfind()屬性)====")
msg = "CIA Vincnet told CIA Esther that USB had given to CIA John"
print("CIA最後出現的位置", msg.rfind("CIA", 0, len(msg)))

print("====分批讀取檔案====")
chuck = 10
msg = ''
with open(fn, encoding="utf-8") as file_obj:
    while True:
        txt = file_obj.read(chuck)
        if not txt:
            break
        msg += txt
print(msg)                    
