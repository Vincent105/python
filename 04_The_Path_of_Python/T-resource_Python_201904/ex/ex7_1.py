# ex7_1.py
files = ['da1.jpg','da2.png','da3.gif','da4.gif',
         'da5.jpg','da6.jpg','da7.gif']
jpg = []
png = []
gif = []
for file in files:
    if file.endswith('.jpg'):   # 以.jpg為副檔名
        jpg.append(file)        # 加入jpg串列
    if file.endswith('.png'):   # 以.png為副檔名
        png.append(file)        # 加入png串列
    if file.endswith('.gif'):   # 以.gif為副檔名
        gif.append(file)        # 加入gif串列
print("jpg檔案串列", jpg)
print("png檔案串列", png)
print("gif檔案串列", gif)







