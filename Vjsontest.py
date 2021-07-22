import requests
import time
import json
import pandas as pd

url = 'http://localhost:9000/api/hotspots/search?projectKey=km&p=1&ps=500&status=TO_REVIEW&onlyMine=false&sinceLeakPeriod=false'
timestr = time.strftime("%Y%m%d_%H%M")
fileOutput = 'SAST_KM' + timestr + '.xlsx'

request = requests.get(url)
jsonload = json.loads(request.text)
print(jsonload)