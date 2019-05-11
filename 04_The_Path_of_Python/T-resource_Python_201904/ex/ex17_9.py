# ex17_9.py
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('d:\\Python\\ex\\data17_9.jpg'),
                                    lang='chi_tra')
print(text)
with open('d:\\Python\\ex\\out17_9.txt', 'w') as fn:
    fn.write(text)


