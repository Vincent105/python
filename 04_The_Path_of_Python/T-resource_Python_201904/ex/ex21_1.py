# ex21_1.py
import json

fn = 'populations.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)                             # 讀json檔案

total = 0
for getData in getDatas:
    if getData['Year'] == '2000':                           # 篩選2000年的數據
        if getData['Country Name'] != "World":
            population = int(float(getData['Numbers']))     # 人口數據
            total += population
            print("%30s   人口數 = %d" % (getData['Country Name'], population))

print('人口總數 = ', total)








        

