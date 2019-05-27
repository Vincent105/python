seasons = {
    'spring': '春',
    'summer': '夏',
    'fall': '秋',
    'winter': '冬'
}

word = input("請輸入季節英文:")
if word in seasons:
    print(word, seasons[word])
else:
    print('無此單字')    