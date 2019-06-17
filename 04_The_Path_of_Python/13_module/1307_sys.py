import sys

for dirpath in sys.path:
    print(dirpath)

print('目前Python系統版本', sys.version)
print('目前平台', sys.platform)
print('目前平台', sys.getwindowsversion())
print('目前平台', sys.executable)

print('請輸入字串=', end='')
msg = sys.stdin.readline()
print(msg)



