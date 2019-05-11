# ex18_1.py
from tkinter import *

window = Tk()
window.title("ex18_1")              # 視窗標題
lab1 = Label(window,text="台塑企業",
              bg="lightyellow",     # 標籤背景是淺黃色
              width=15)             # 標籤寬度是15
lab2 = Label(window,text="台積電",
              bg="lightgreen",      # 標籤背景是淺綠色
              width=15)             # 標籤寬度是15
lab3 = Label(window,text="宏碁電腦",
              bg="lightblue",       # 標籤背景是淺藍色
              width=15)             # 標籤寬度是15
lab4 = Label(window,text="華碩電腦",
              bg="lightpink",       # 標籤背景是淺粉色
              width=15)             # 標籤寬度是15
lab5 = Label(window,text="華碩電腦",
              bg="aqua",            # 標籤背景是水藍色
              width=15)             # 標籤寬度是15
lab1.pack()                         # 包裝與定位元件
lab2.pack()                         # 包裝與定位元件
lab3.pack()                         # 包裝與定位元件
lab4.pack()                         # 包裝與定位元件
lab5.pack()                         # 包裝與定位元件

window.mainloop()






