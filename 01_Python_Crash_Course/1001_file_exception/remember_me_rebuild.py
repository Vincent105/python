# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
import json

def get_stored_name():
    '''如果已經儲存，就直接取得名字'''
    filename = '01_Python_Crash_Course\\1001_file_exception\\username.json'
    try:
        with open(filename) as fileobject:
            username = json.load(fileobject)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''要求輸入名字，並且進行儲存'''
    username = input("What is your name?")
    filename = '01_Python_Crash_Course\\1001_file_exception\\username.json'
    with open(filename, 'w') as fileobject:
        json.dump(username, fileobject)
        return username

def greeting():
    '''判別名字，並進行問候'''
    username = get_stored_name()
    if username:
        print('Welcome back,' + username)
    else:
        username = get_new_username()
        print("We will remember you when you come back, " + username + "!")   

greeting()
