# ex14_3.py
import os
totalsizes = 0
totalfiles = 0

mydir = input("請輸入目錄 : ")
if os.path.exists(mydir):
    for file in os.listdir(mydir):
        size = os.path.getsize(os.path.join(mydir,file))
        print(file, ":", size)
        totalsizes += size
        totalfiles += 1
    print("全部檔案數量是 = ", totalfiles)    
    print("全部檔案大小是 = ", totalsizes)
else:
    print(mydir,"目錄不存在")
    
    





    
