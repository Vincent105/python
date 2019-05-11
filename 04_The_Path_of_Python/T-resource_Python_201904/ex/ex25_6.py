# ex25_6.py
import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[1000, 850, 800, 1500, 600, 800],
          'area':[400, 500, 850, 300, 200, 320],
          'town':['New York','Chicago','Bangkok','Tokyo',
                   'Singapore','HongKong']}

tw = pd.DataFrame(cities,
                  columns=['population','area','density'],index=cities['town'])
density = tw['population'].div(cities['area'])
tw['density'] = density
print(tw)


fig, ax = plt.subplots()
fig.suptitle("City Statistics")

ax.set_ylabel("Population and Area")
ax.set_xlabel("City")

ax2 = ax.twinx()
ax2.set_ylabel("Density")
tw['population'].plot(ax=ax,rot=90)     # 繪製人口數線
tw['area'].plot(ax=ax, style='g-')     # 繪製面積線
tw['density'].plot(ax=ax2, style='r-')     # 繪製密度線
ax.legend(loc=2)                        # 圖例位置在右上
ax2.legend(loc=1)                       # 圖例位置在左上

plt.show()








