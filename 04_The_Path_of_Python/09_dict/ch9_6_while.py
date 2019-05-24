survey_dict = {}
market_survey = True

while market_survey:
    name = input("請輸入姓名:")
    travel_place = input("請輸入你希望的旅遊地點:")

    survey_dict[name] = travel_place
    
    repeat = input("是否繼續輸入其他資料:(y/n):")
    if repeat == 'n':
        market_survey = False

print("以下是調查的結果:\n")
for name, place in survey_dict.items():
    print("%s喜歡的旅遊地點是%s"%(name, place))
