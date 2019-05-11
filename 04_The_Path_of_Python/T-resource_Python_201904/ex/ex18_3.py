# ex18_3.py
from tkinter import *
def oper():                                  # 加法運算
    op = x.get()
    if op == '+':
        n3.set(n1.get()+n2.get())
    elif op == '-':
        n3.set(n1.get()-n2.get())
    elif op == '*':
        n3.set(n1.get()*n2.get())
    elif op == '/':
        n3.set(n1.get()/n2.get())

def myadd():
    x.set('+')
def mysub():
    x.set('-')
def mymul():
    x.set('*')
def mydiv():
    x.set('/')
    
window = Tk()
window.title("ex18_3")                      # 視窗標題

n1 = IntVar()                   
n2 = IntVar()
n3 = IntVar()
x = StringVar()

e1 = Entry(window,width=8,textvariable=n1)  # 文字方塊1
label = Label(window,width=3,textvariable=x)
btnadd = Button(window,width=3,text='+',command=myadd)    # 加號
btnsub = Button(window,width=3,text='-',command=mysub)    # 減號
btnmul = Button(window,width=3,text='*',command=mymul)    # 乘號
btndiv = Button(window,width=3,text='/',command=mydiv)    # 除號
e2 = Entry(window,width=8,textvariable=n2)  # 文字方塊2
btn = Button(window,width=5,text='=',command=oper)        # =按鈕
e3 = Entry(window,width=8,textvariable=n3)  # 儲存結果文字方塊

e1.grid(row=0,column=0)                     # 定位文字方塊1
label.grid(row=0,column=1,padx=5)           # 定位加號
e2.grid(row=0,column=2)                     # 定位文字方塊2
btnadd.grid(row=1,column=1,padx=5)          # 定位加號
btnsub.grid(row=2,column=1,padx=5)          # 定位加號
btnmul.grid(row=3,column=1,padx=5)          # 定位加號
btndiv.grid(row=4,column=1,padx=5)          # 定位加號
btn.grid(row=5,column=1,pady=5)             # 定位=按鈕
e3.grid(row=6,column=1)                     # 定位儲存結果

window.mainloop()






