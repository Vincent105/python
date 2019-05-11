# ex18_9.py
from tkinter import *
from tkinter import messagebox

def newfile():
    messagebox.showinfo("開新檔案","可在此撰寫開新檔案程式碼")    
def savefile():
    messagebox.showinfo("儲存檔案","可在此撰寫儲存檔案程式碼")
def delMsg():
    messagebox.showinfo("剪下內容","可在此剪下文件內容")
def copyMsg():
    messagebox.showinfo("複製內容","可在此複製文件內容")
def pasteMsg():
    messagebox.showinfo("貼上內容","可在此貼上文件內容")
    
def about():
    messagebox.showinfo("程式說明","作者:洪錦魁")

window = Tk()
window.title("ex18_9")
window.geometry("300x160")          # 視窗寬300高160

menu = Menu(window)                 # 建立功能表物件
window.config(menu=menu)

filemenu = Menu(menu)               # 建立檔案功能表
menu.add_cascade(label="檔案",menu=filemenu)
filemenu.add_command(label="開新檔案",command=newfile)
filemenu.add_separator()            # 增加分隔線
filemenu.add_command(label="儲存檔案",command=savefile)
filemenu.add_separator()            # 增加分隔線
filemenu.add_command(label="結束",command=window.destroy)

editmenu = Menu(menu)               # 建立檔案功能表
menu.add_cascade(label="編輯",menu=editmenu)
editmenu.add_command(label="剪下",command=delMsg)
editmenu.add_command(label="複製",command=copyMsg)
editmenu.add_separator()            # 增加分隔線
editmenu.add_command(label="貼上",command=pasteMsg)

helpmenu = Menu(menu)               # 建立說明功能表
menu.add_cascade(label="說明",menu=helpmenu)
helpmenu.add_command(label="程式說明",command=about)

mainloop()






