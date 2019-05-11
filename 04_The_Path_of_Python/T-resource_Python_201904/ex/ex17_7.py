# ex17_7.py
import qrcode

codeText = 'http://www.mcut.edu.tw'
img = qrcode.make(codeText)                 # 建立QR code 物件
print("檔案格式", type(img))
img.save("fig17_7.jpg")


