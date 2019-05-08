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

#逐行讀取文檔並且存放於列表
filename = '01_Python_Crash_Course\\1001_file_exception\\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())    

#使用文件的內容
filename =  '01_Python_Crash_Course\\1001_file_exception\\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
print(type(pi_string))

#讀取大量數據
filename_2 =   '01_Python_Crash_Course\\1001_file_exception\\pi_million_digits.txt'

with open(filename_2) as fileobject:
    lines = fileobject.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:52] + '...')    
