# ex22_5.py
import csv
import matplotlib.pyplot as plt
from datetime import datetime

fn = 'TaipeiWeatherJan.csv'
with open(fn) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)             # 讀取文件下一行
    dates, highTemps, meanTemps, lowTemps = [], [], [], [] # 設定空串列
    for row in csvReader:
        try:                    
            currentDate = datetime.strptime(row[0], "%Y/%m/%d")
            highTemp = int(row[1])          # 設定最高溫
            meanTemp = int(row[2])          # 設定均溫
            lowTemp = int(row[3])           # 設定最低溫
        except Exception:
            print('有缺值')
        else:
            highTemps.append(highTemp)      # 儲存最高溫
            meanTemps.append(meanTemp)      # 儲存均溫
            lowTemps.append(lowTemp)        # 儲存最低溫
            dates.append(currentDate)       # 儲存日期

fig = plt.figure(dpi=80, figsize=(12, 8))   # 設定繪圖區大小
plt.plot(dates, highTemps, label='High')    # 繪製最高溫
plt.plot(dates, meanTemps, label='Mean')    # 繪製均溫
plt.plot(dates, lowTemps, label='Low')      # 繪製最低溫
plt.fill_between(dates, highTemps, meanTemps, color='y', alpha=0.2) # 填滿區間
plt.fill_between(dates, meanTemps, lowTemps, color='r', alpha=0.2)  # 填滿區間
fig.autofmt_xdate()                         # 日期旋轉
plt.title("Weather Report, Jan. 2017", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature (C)", fontsize=14)
plt.tick_params(axis='both', labelsize=12, color='red')
plt.legend(loc='best')
plt.show()


