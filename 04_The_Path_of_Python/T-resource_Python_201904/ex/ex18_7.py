# ex18_7.py
from tkinter import *
from tkinter import messagebox

def printInfo():                    # 列印輸入資訊
    if e1.get() in accountDict:
        if e2.get() == accountDict[e1.get()]:
            messagebox.showinfo("歡迎進入系統")
        else:
            messagebox.showinfo("密碼錯誤")
    else:
        messagebox.showinfo("帳號錯誤")

accountDict = {"AAA":"1234", "BBB":"2345", "CCC":"3456"}
         
window = Tk()
window.title("ex18_7")              # 視窗標題

lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Password").grid(row=1)

xAccount = StringVar()
xPassword = StringVar()

e1 = Entry(window,textvariable=xAccount)        # 文字方塊1
e2 = Entry(window,textvariable=xPassword)       # 文字方塊2
e1.grid(row=0,column=1)             # 定位文字方塊1
e2.grid(row=1,column=1)             # 定位文字方塊2

btn = Button(window,text="確定",command=printInfo)
# sticky=W可以設定物件與上面的Label切齊, pady設定上下間距是10
btn.grid(row=2,column=1,pady=10)  

window.mainloop()






