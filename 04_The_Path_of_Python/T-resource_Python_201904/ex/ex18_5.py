# ex18_5.py
from tkinter import *
def printSelection():
    x.set(cities[var.get()])              # 列出所選城市

window = Tk()
window.title("ex18_5")                  # 視窗標題
cities = {0:"東京",1:"紐約",2:"巴黎",3:"倫敦",4:"香港"}

var = IntVar()
var.set(0)                              # 預設選項                       
label = Label(window,text="選擇最喜歡的城市",
              fg="blue",bg="lightyellow",width=30)
label.pack()

for val, city in cities.items():        # 建立選項紐    
    Radiobutton(window,
                text=city,
                variable=var,value=val,
                command=printSelection).pack()
    
x = StringVar()
display = Label(window,textvariable=x, bg="lightgreen",width=30)
display.pack()

window.mainloop()






