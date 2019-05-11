# ex5_5.py
i = input("溫度轉換選擇\n1:華氏溫度轉成攝氏溫度\n2:攝氏溫度轉華氏溫度\n= ")
if i == "1":
    f = input("請輸入華氏溫度：")
    c = ( int(f) - 32 ) * 5 / 9
    print("華氏 %s 等於攝氏 %4.1f" % (f, c))    
elif i == "2":    
    c = input("請輸入攝氏溫度：")
    f = int(c) * 9 / 5 + 32
    print("攝氏 %s 等於華氏 %4.1f" % (c, f))
else:
    print("輸入錯誤")


