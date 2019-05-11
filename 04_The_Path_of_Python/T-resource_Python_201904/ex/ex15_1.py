# ex15_1.py

msg = input("請輸入文字 : ")
with open("in15_6.txt", "w") as fobj:
    fobj.write(msg)
fn = "in15_6.txt"
    
try:
    with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print("找不到 %s 檔案" % fn)
else:
    wordList = data.split()     # 將文章轉成串列
    print(fn, " 文章的字數是 ", len(wordList))    # 列印文章字數





