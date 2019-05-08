import json

number = [2, 3, 5, 7, 11, 13]

filename = '01_Python_Crash_Course\\1001_file_exception\\number.json'

with open(filename, 'w') as fileobject:
    json.dump(number, fileobject)       #json.dump 包含兩個變數:要存储的数据以及可用于存储数据的文件。
