# ex21_3.py
import pygal.maps.world

worldMap = pygal.maps.world.World()         # 建立世界地圖物件
worldMap.title = 'Word Language'            # 世界地圖標題
worldMap.add('English-speaking countries',['us', 'au', 'ca', 'gb', 'nz'])   
worldMap.add('Arabic-speaking countries',['ae', 'eg', 'ye', 'kw', 'sa'])     
worldMap.add('German-speaking countries',['de', 'at', 'ch', 'lu', 'li'])     
worldMap.render_to_file('out21_3.svg')     # 儲存地圖檔案





