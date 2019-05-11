# ex17_1.py
from PIL import Image

pict = Image.open("hung.jpg")                        # 建立Pillow物件
width, height = pict.size
newPict1 = pict.resize((int(width*1.2), height))     # 寬度是1.2倍
newPict1.save("out17_1.jpg")

newPict2 = pict.resize((int(width*1.5), height))     # 寬度是1.5倍
newPict2.save("out17_2.jpg")

newPict3 = pict.resize((int(width*0.5), height))     # 寬度是0.5倍
newPict3.save("out17_3.jpg")

newPict4 = pict.resize((int(width*0.8), height))     # 寬度是0.8倍
newPict4.save("out17_4.jpg")

newPict5 = pict.resize((width, int(height*1.2)))     # 高度是1.2倍
newPict5.save("out17_5.jpg")

newPict6 = pict.resize((width, int(height*1.5)))     # 高度是1.5倍
newPict6.save("out17_6.jpg")

newPict7 = pict.resize((width, int(height*0.8)))     # 高度是0.8倍
newPict7.save("out17_7.jpg")

newPict8 = pict.resize((width, int(height*0.5)))     # 高度是0.5倍
newPict8.save("out17_8.jpg")


