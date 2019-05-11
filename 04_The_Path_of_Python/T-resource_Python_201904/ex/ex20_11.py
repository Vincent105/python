# ex20_11.py
import matplotlib.pyplot as plt
from pylab import mpl
import twstock

mpl.rcParams["font.sans-serif"] = ["SimHei"]        # 使用黑體
seq = list(range(0, 31))

stock2330 = twstock.Stock("2330")

linePrice, = plt.plot(seq, stock2330.price, '-*', label='收盤價')
lineHigh, = plt.plot(seq, stock2330.high, '-o', label='最高價')
lineLow, = plt.plot(seq, stock2330.low, '-^', label='最低價')

plt.legend(handles=[linePrice, lineHigh, lineLow], loc='best')
plt.title(u"台積電", fontsize=24)
plt.xlabel("近31個交易日", fontsize=14)
plt.ylabel("價格", fontsize=14)
plt.show()

