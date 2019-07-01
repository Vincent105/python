import os
import glob

print(os.getcwd())
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.abspath('1401_os.py'))

print(os.path.relpath('E:\\'))

mydir = 'test14'
myfile = 'test.py'

if os.path.exists(mydir):
    print("已經存在%s" % mydir)
else:
    os.mkdir(mydir)
    print("建立成功%s" % mydir)

if os.path.exists(mydir):
    os.rmdir(mydir)
    print("刪除成功%s" % mydir)
else:
    print("不存在%s" % mydir)

if os.path.exists(myfile):
    os.remove(myfile)
    print("刪除成功%s" % myfile)
else:
    print("不存在%s" % myfile)

print(os.path.join('D:\\', 'Python', '14_white_read'))

files = ['ch14_1.py', 'ch14_2.py']
for file in files:
    print(os.path.join('D:\\', 'Python', '14_white_read\\') + file)

print(os.path.getsize('04_The_Path_of_Python\\14_write_read\\1401_os.py'))
print(os.listdir('04_The_Path_of_Python\\13_module'))

totalsize = 0
for file in os.listdir('04_The_Path_of_Python\\13_module'):
    print(file)
    totalsize += os.path.getsize(os.path.join(
        'E:\python\\04_The_Path_of_Python\\13_module', file))
print('file size is:', totalsize)

print("glob方法一：列出特定目錄的所有檔案")
for file in glob.glob("E:\\python\\04_The_Path_of_Python\\13_module\\*.*"):
    print(file)

print("glob方法二：列出特定目錄的特定")
for file in glob.glob(r'E:\\python\\04_The_Path_of_Python\\13_module\\131*.py'):
    print(file)

print("glob方法三：列出特定目錄的特定檔案")
for file in glob.glob(r'E:\\python\\04_The_Path_of_Python\\13_module\\131*.*'):
    print(file)

for dirname,sub_dirnames,filenames in os.walk("E:\\python\\04_The_Path_of_Python\\13_module"):
    print("目錄名稱",dirname)
    print("子目錄名稱",sub_dirnames)
    print("檔案名稱",filenames)