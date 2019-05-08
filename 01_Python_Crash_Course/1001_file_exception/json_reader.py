import json

filename = '01_Python_Crash_Course\\1001_file_exception\\number.json'
with open(filename) as fileobject:
    numbers = json.load(fileobject)

print(numbers)