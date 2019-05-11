# ex8_6.py
weatherH = (30, 28, 29, 31, 33, 35, 32)
weatherL = (20, 21, 19, 22, 23, 24, 20)
print("過去一周的最高溫度 %d " % max(weatherH))
print("過去一周的最低溫度 %d " % min(weatherH))

print("過去一周的平均溫度")     
for i in range(len(weatherH)):
    print("%3.1f  " % ((weatherH[i]+weatherL[i])/2), end="")
          


