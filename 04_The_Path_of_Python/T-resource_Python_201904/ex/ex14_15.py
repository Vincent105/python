# ex14_15.py
import string

def encrypt(text, encryDict):           # 加密文件
    cipher = []
    for i in text:                      # 執行每個字元加密
        v = encryDict[i]                # 加密
        cipher.append(v)                # 加密結果
    return ''.join(cipher)              # 將串列轉成字串

def decrypt(cipher, decryDict):         # 解密文件
    text = []
    for i in cipher:                    # 執行每個字元解密
        v = decryDict[i]                # 加密
        text.append(v)                  # 解密結果
    return ''.join(text)                # 將串列轉成字串
    
abc = string.printable[:-3]             # 取消不可列印字元
subText = abc[-3:] + abc[:-3]           # 加密字串字串
encry_dict = dict(zip(subText, abc))    # 建立字典
decry_dict = dict(zip(abc, subText))    # 建立解密字典
fn = "zenofPython.txt"
with open(fn) as file_Obj:              # 開啟檔案
    msg = file_Obj.read()               # 讀取檔案
    
ciphertext = encrypt(msg, encry_dict)

outEn = "zenofPython_Encry.txt"
with open(outEn, 'w') as file_out:
    file_out.write(ciphertext)

decrytext = decrypt(ciphertext, decry_dict)

outDe = "zenofPython_Decry.txt"
with open(outDe, 'w') as file_out:
    file_out.write(decrytext)











