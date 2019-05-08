# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
import json

filename = '01_Python_Crash_Course\\1001_file_exception\\username.json'

try:
    with open(filename) as fileobject:
        username = json.load(fileobject)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename, 'w') as fileobject:
        json.dump(username, fileobject)
        print("We will remember you when you come back, " + username + "!")   
else:
    print('Welcome back,' + username)

