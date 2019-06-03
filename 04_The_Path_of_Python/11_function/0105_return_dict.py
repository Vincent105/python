def build_vip(id, name, tel=''):
    '''建立VIP資料'''
    vip_dict = {'VIP_ID': id, 'Name': name}
    if tel:
        vip_dict['tel'] = tel
    return vip_dict


while True:
    print("vip建立系統")
    id_num = input("請輸入vip帳號:")
    name = input("請輸入vip姓名:")
    tel = input("請輸入vip電話(按enter可跳過輸入):")
    member = build_vip(id_num, name, tel)
    print(member, '\n')
    repeat = input("是否繼續輸入Y/N")
    if repeat != 'Y':
        break
print("歡迎再度使用")
