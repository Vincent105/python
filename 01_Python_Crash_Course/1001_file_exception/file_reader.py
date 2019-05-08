#取得工作路徑
import os
cwd = os.getcwd() 
files = os.listdir(cwd) 
print("Files in '%s': %s" % (cwd, files))

##讀取文檔
with open('01_Python_Crash_Course\\1001_file_exception\\pi_digits.txt') as file_object:
    content = file_object.read()
    print(content.rstrip())

#逐行讀取文檔
filename = '01_Python_Crash_Course\\1001_file_exception\\pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
