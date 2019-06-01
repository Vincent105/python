def guest_info(firstname, lastname, gender, middlename=''):
    ''''''
    if gender == "M":
        welcome = "Welcome " + lastname + middlename + firstname + "先生歡迎"
    else:
        welcome = "Welcome " + lastname + middlename + firstname + "小姐歡迎"
    return welcome


info1 = guest_info("宗", "洪", "M")
info2 = guest_info("宗", "王", "F", "星")
print(info1)
print(info2)
