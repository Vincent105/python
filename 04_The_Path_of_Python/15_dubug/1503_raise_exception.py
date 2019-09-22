import traceback

def passWord(pwd):
    """check the password lens between 4~8"""
    pwdLen = len(pwd)
    if pwdLen < 4:
        raise Exception("The password is too short.")
    if pwdLen > 8:
        raise Exception("tHE password is too long")
    else:
        print('the length of the password is correct.')
        
for pwd in ('aaaaaaaaaa', 'aaa', 'aaaaa'):
    try:
        passWord(pwd)
    except Exception as err:
        errlog = open('04_The_Path_of_Python\\15_dubug\\log.txt', 'a')
        errlog.write(traceback.format_exc())
        errlog.close()
        print('寫入異常')
        print('異常訊息:' + str(err))
