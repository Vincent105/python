import requests
import logging

logging.captureWarnings(True)               #透過偵測警告來忽略警告。
response = requests.get('https://ps.solventosoft.com.tw:8443/redmine',verify=False)
print(response.status_code)