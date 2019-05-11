# ex10_1.py
txt = '''Silicon Stone Education is an unbiased organization,
concentrated on bridging the gap between academic and the
working world in order to benefit society as a whole.
We have carefully crafted our online certification system
and test content databases. The content for each topic is
created by experts and is all carefully designed with a
comprehensive knowledge to greatly benefit all candidates
who participate.
'''
txtLower = txt.lower()          # 改為小寫
for ch in txtLower:
    if ch in ".,?":
        txtLower = txtLower.replace(ch,'')

txtLst = txtLower.split()       # 將文件轉成串列
setX = set(txtLst)              # 將串列轉成集合
lst = list(setX)                # 將集合轉成串列
print("最後串列 = ", sorted(lst))







