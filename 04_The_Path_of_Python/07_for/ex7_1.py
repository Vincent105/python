images = ['da1.jpg', 'da2.png', 'da3.gif', 
          'da4.gif', 'da5.jpg', 'da6.jpg', 'da7.gif'
]
jpgs = []
pngs = []
gifs = []

for image in images:
    if image.endswith('.jpg'):
        jpgs.append(image)
    if image.endswith('.png'):
        pngs.append(image)
    if image.endswith('.gif'):
        gifs.append(image)    
print("jpg檔案串列", jpg)
print("png檔案串列", png)
print("gif檔案串列", gif)