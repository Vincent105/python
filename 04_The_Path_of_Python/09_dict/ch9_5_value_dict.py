chat_account = {
    'cshung':{
        'last_name': '洪',
        'first_name': 'XX',
        'city': '台北'
    },
    'kevin':{
        'last_name': '王',
        'first_name': 'OO',
        'city': '高雄'
    }
}

for key , value_set in chat_account.items():
    print('聯絡人%s:'%key)
    print('中文姓名:' +  value_set['last_name'] + value_set['first_name'])
    print('居住地區是:' + value_set['city'])

print(len(chat_account))
print(len(chat_account['cshung']))