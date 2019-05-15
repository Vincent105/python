#判斷文件檔案格式
files = ['dac1.c', 'dac2.py', 'da3.py','da4,java']
py = []
for file in files:
    if file.endswith('.py'):
        py.append(file)
print(py)    

names = ['王OO', '王XX', '陳OO', '黃XX']
namecontent = []

for name in names:
    if name.startswith('王'):
        namecontent.append(name)
print(namecontent)
