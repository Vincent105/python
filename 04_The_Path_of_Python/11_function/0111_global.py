def printlocal():
    global msg
    msg = 'C#'
    print(msg)
    print(locals())

msg = 'Python'
printlocal()
print(globals())