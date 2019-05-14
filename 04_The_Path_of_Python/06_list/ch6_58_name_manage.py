accounts = []
account = input('請輸入新帳號:')
accounts.append(account)

print("公司系統")
ac = input("請輸入帳號:")
if ac in accounts:
    print("歡迎進入公司系統")
else:
    print("帳號錯誤")    

