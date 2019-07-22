import pandas as pd 
import numpy as np 

print("csv包含欄位表頭讀取方式")
df1 = pd.read_csv('\\python\\A03_Machine_learning\\E01_python_for_data_analysis\\examples\\ex1.csv')
print(df1)    

df2 = pd.read_table('\\python\\A03_Machine_learning\\E01_python_for_data_analysis\\examples\\ex1.csv',sep=',')
print(df2)    

print("csv沒有欄位表頭讀取方式")
df = pd.read_csv('\\python\\A03_Machine_learning\\E01_python_for_data_analysis\\examples\\ex2.csv',header=None)
print(df)    

df = pd.read_csv('\\python\\A03_Machine_learning\\E01_python_for_data_analysis\\examples\\ex2.csv',names=['a','b','c','d','message'])
print(df)    

print("csv指定某個欄位作為索引，通过index_col参数指定：")
names = ['a','b','c','d','message']
pf = pd.read_csv('\\python\\A03_Machine_learning\\E01_python_for_data_analysis\\examples\\ex2.csv',names=names,index_col='message')
print(pf)    

print("csv階層式索引，通过index_col参数傳入列表：")
parsed = pd.read_csv('\\python\\A03_Machine_learning\\E01_python_for_data_analysis\\examples\\csv_mindex.csv',index_col=['key1','key2'])
print(parsed)    

print("通过index_col参数：跳過讀取文檔的部分行")
pf = pd.read_csv('\\python\\A03_Machine_learning\\E01_python_for_data_analysis\\examples\\ex4.csv',skiprows=[0,2,3])
print(pf)    

result = pd.read_csv('\\python\\A03_Machine_learning\\E01_python_for_data_analysis\\examples\\ex5.csv')
print(result)    

 