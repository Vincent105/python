#寫入空文字檔
filename = '01_Python_Crash_Course\\1001_file_exception\\programming.txt'

with open(filename, 'w') as fileobject:             # 'r' 'w' 'a' 'r+'
    fileobject.write('I love python\n')
    fileobject.write('I love c#\n')    

with open(filename, 'a') as fileobject:             # 'r' 'w' 'a' 'r+'
    fileobject.write('I love python++++++\n')
    fileobject.write('I love c#++++++\n')