import pandas as pd 
import pandas_datareader.data as web
from datetime import datetime

f = web.DataReader('USD000UTSTOM', 'moex', start='2017-07-01', end='2017-07-31')
print(f.head())