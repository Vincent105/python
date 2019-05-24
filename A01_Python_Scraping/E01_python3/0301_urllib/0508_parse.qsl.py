from urllib.parse import parse_qsl

#反向序列化，轉換回tuple
query = 'name=gemery&age=22'
print(parse_qsl(query))