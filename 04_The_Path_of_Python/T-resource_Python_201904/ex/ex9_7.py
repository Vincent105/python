# ex9_7.py
# 建立內含字典的字典
travel = {'張家界':{'state':'湖南省',
                    'attraction':'天門山, 大峽谷'},
          '九寨溝':{'state':'四川省',
                    'attraction':'熊貓海, 箭竹海'},
          '黃山':{'state':'安徽省',
                  'attraction':'天都峰, 蓬萊三島'},
          '武夷山':{'state':'福建省',
                    'attraction':'天遊峰, 桃源洞'},
          '敦煌':{'state':'甘肅省',
                  'attraction':'石窟, 月牙泉'}}
# 列印內含字典的字典
for loc, info in travel.items( ):
    print("旅遊地點 = ", loc)                      # 列印鍵(key)
    print("省份     = ", info['state'])          # 列印值(value)
    print("景點     = ", info['attraction'])     # 列印值(value)

