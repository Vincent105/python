# ex13_9.py
import keyword

while True:
    word = input("輸入字串 : ")
    if word in keyword.kwlist:
        print(word, "是關鍵字")
    else:
        print(word, "不是關鍵字")
    if word == 'Q' or word == 'q':
        break






