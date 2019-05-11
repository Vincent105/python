# ex16_1.py
def chinaPhoneNum(string):
    """檢查是否有含手機聯絡資訊的台灣手機號碼格式"""
    if len(string) != 13:       # 如果長度不是13
        return False            # 傳回非手機號碼格式
    
    for i in range(0, 3):       # 如果前3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格式
        
    if string[3] != '-':        # 如果不是'-'字元
        return False            # 傳回非手機號碼格式
   
    for i in range(4, 8):       # 如果中間4個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格

    if string[8] != '-':        # 如果不是'-'字元
        return False            # 傳回非手機號碼格式

    for i in range(9, 13):      # 如果最後4個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格
    return True                 # 通過以上測試

print("I love Ming-Chi: 是大陸手機號碼", chinaPhoneNum('I love Ming-Chi'))
print("0932-999-199:    是大陸手機號碼", chinaPhoneNum('0932-999-199'))
print("133-1234-1234:   是大陸手機號碼", chinaPhoneNum('133-1234-1234'))
