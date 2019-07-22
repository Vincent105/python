# 內建模組
import os                               #        
import glob                             #取得特定工作目錄內容
import shutil                           #檔案或目錄複製、刪除、移動、更改名稱
import time                             #時間模組
import math                             #數學模組
import pprint		                    #漂亮列印字典
import copy			                    #複製列表或字典
from random import randint              #生成隨機數
import json                             #将数据结构转储文件，并在程序再次运行时加载该文件中的数据。在程序之间分享数据 
import unittest                         #代碼測試工具
import re                               #正規表達式
import locale                           #獲取系統編碼

from collections import OrderedDict     #紀錄鍵-值添加順序
from collections import defaultdict     #自動初始化每個 key 剛開始對應的值
from collections import counter         #計數器
from collections import deque           #構造函數

import matplotlib.pyplot as plt         #繪圖用
from operator import itemgetter         #通過某個關鍵字排序一個字典列表








# 額外模組
import pyperclip	                    #複製字符串
import send2trash                       # python -m pip install send2trash 



'''
爬蟲相關套件
'''
# 請求(第三方套件)
import requests                         # python -m pip install requests         模擬瀏覽器向伺服器發出請求
import selenium                         # python -m pip install selenium         驅動瀏覽器執行特定動作
import aiohttp                          # python -m pip install aiohttp          提供同步WEB服務 
                                        # python -m pip install cchardet         字符編碼檢測套件
                                        # python -m pip install aiodns           加速DNS檢析套件 

# 模擬器chrome                               https://chromedriver.storage.googleapis.com/index.html
# 模擬器filefox                              https://github.com/mozilla/geckodriver/releases
# 無介面可腳本編譯的瀏覽器引擎PhantomJS        http://phantomjs.org/download.html   

# MS-SQL                                # python -m pip install python-sql
 
# 解析(第三方套件)
import bs4                              # python -m pip install bs4        
import lxml                             # python -m pip install lxml          更強大的html parser,速度較快
import html5lib                         # python -m pip install html5lib      解決格式問題，但速度較慢
import pyquery                          # python -m pip install pyquery


# OCR                                   # python -m pip install tesseract
import tesserocr                        # 透過cmd 下指令cd C:\Python3X\Scripts pip install tesserocr-2.4.0-cp37-cp37m-win32.whl                                        


# Web套件
import flask                            # python -m pip install flask      
import tornado                          # python -m pip install tornado      

# 擷取框架
'''scrapy'''                            # python -m pip install pyopenssl
                                        # 透過cmd 下指令cd C:\Python3X\Scripts pip install Twisted-19.2.0-cp37-cp37m-win32.whl
                                        # python -m pip install pywin32
                                        # python -m pip install scrapy                                        
'''pyspider'''

                                        # 透過cmd 下指令cd C:\Python3X\Scripts pip install pycurl-7.43.0.2-cp37-cp37m-win32.whl                                     
                                        # python -m pip install pyspider      


'''
#Machine Learning
'''
import keras                            # pip install keras
import tensorflow                       # pip install tensorflow-gpu
import numpy                            # pip install numpy==1.16.2
import tensorboard                      # pip install tensorboard
                                        # pip install scipy
import Matplotlib                       # pip install Matplotlib
import pandas                           # pip install pandas
import pandas_datareader                # pip install pandas_datareader