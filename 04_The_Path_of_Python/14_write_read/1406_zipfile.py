import zipfile
import glob
import os

# 進行檔案壓縮
filezip = zipfile.ZipFile(
    '04_The_Path_of_Python\\test.zip', 'w')

for name in glob.glob("04_The_Path_of_Python\\14_write_read\\*"):
    filezip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)

filezip.close()

# 讀取壓縮檔
listZipInfo = zipfile.ZipFile(
    '04_The_Path_of_Python\\test.zip', 'r')

print(listZipInfo.namelist())
print('\n')
for info in listZipInfo.infolist():
    print(info.filename, info.file_size, info.compress_size)

# 解壓縮zip
fileUnZip = zipfile.ZipFile('04_The_Path_of_Python\\test.zip')
fileUnZip.extractall("test")
fileUnZip.close()

