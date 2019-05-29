'''
match()，只能夠從開頭處開始進行比對
'''
# match()
import re

# 基本re match()
content = 'Hello 123 4567 World_This is a Regex Demo'
print(content)

result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}', content)
print(result)
print(result.group())
print(result.span())

# 匹配目標透過 group()  group(1)呈現
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\s(World)', content)

print(result)
print(result.group())
print(result.span())
print(result.group(1))  # 輸出第一個()包圍
print(result.group(2))  # 輸出第二個()包圍

# 通用匹配 透過.* 進行簡化
result = re.match('^Hello.*Demo$', content)
print(result.group())

# 貪婪(.*) 及 非貪婪(.*?)。建議盡量使用非貪婪比對
# .*  貪婪:盡可能的比對越多越好，故比對了123456。保留\d+ ==> 7 至少一個以上的數值。
result = re.match('^He.*(\d+).*Demo$', content)
print(result.group(1))

# .*? 非貪婪:盡可能的匹配越少越好。.*?就不進行比對，交給\d+進行比對
result = re.match('^He.*?(\d+).*Demo$', content)
print(result.group(1))

# 但非貪婪(.*?)放在結尾時，有可能比對不到任何內容
content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http.*?comment/(.*?)', content)
result2 = re.match('http.*?comment/(.*)', content)
print(result1, result1.group(1))
print(result2, result2.group(1))

# 修飾參數 透過(re.S):比對包含換行符號在內的所有字符   (re.I):使比對對大小寫不敏感
content = '''Hello 1234567 World_This 
is a Regex Demo
'''
result = re.match('He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))

# 轉義比對 (\)
content = '(谷歌)www.google.com'
result = re.match('^\(谷歌\)www\.google\.com$', content)
print(result.group())
