# ex14_1.py
import os

mydir = input("請輸入目錄 : ")
if os.path.exists(mydir):
    print(mydir, "已經存在")
else:
    print("目錄不存在")
    os.mkdir(mydir)
    print("建立此目錄")
    





    
