import json

filename = '01_Python_Crash_Course\\1001_file_exception\\username.json'
with open(filename) as fileobject:
    usergreeting = json.load(fileobject)
    print(usergreeting + ' welcome come back.')
