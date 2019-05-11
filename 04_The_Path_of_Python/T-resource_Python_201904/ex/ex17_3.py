# ex17_3.py
from PIL import Image

mywidth, myheight = 99, 127
hungPic = Image.open("hung.jpg")                # 建立Pillow物件
width, height = hungPic.size
newPic = hungPic.resize((mywidth, myheight))

width, height = 634, 548                        # 新影像寬與高
newImage = Image.new('RGB', (width, height), "Yellow")  # 建立新影像
for x in range(20, width-20, mywidth):          # 雙層迴圈合成
    for y in range(20, height-20, myheight):
        newImage.paste(newPic, (x, y))          # 合成

newImage.save("fig17_3.jpg")                    # 儲存









