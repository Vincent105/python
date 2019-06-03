import re

content1 = '2016-12-15 12:00'
content2 = '2016-12-15 16:00'
content3 = '2016-12-15 18:00'

pattern = re.compile('\d{2}:\d{2}')

content1 = re.sub(pattern, '', content1)
content2 = re.sub(pattern, '', content2)
content3 = re.sub(pattern, '', content3)
print(content1, content2, content3)
