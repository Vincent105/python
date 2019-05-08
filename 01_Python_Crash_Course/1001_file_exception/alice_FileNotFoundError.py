filename = 'alice.txt'

try:
    with open(filename) as fileobject:
        contents = fileobject.read()
except FileNotFoundError:
    msg = 'We can not find ' + filename + ' in your file.'
    print(msg)
else:
    print(contents)    
