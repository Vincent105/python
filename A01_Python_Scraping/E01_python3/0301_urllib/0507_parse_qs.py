from urllib.parse import parse_qs

#反向序列化，轉換回字典
query = 'name=germey&age=22'
print(parse_qs(query))

