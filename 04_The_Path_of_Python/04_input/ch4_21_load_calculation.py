load = eval(input('請輸入你的貸款金額：'))
year = eval(input('請輸入你的貸款年限：'))
rate = eval(input('請輸入你的貸款利率：'))
monthRate = rate / (12 * 100)

#計算每月還款金額
molecules = load * monthRate
denominator = 1 - (1 / (1 + monthRate) ** (year * 12))
monthPay = molecules / denominator              #每月還款金額
totalPay = monthPay * year * 12                 #總計還款金額
print('每月還款金額為%10f:'% int(monthPay))
print('總共還款金額為%10f:'% int(totalPay))