import re 

#匹配最長 或者最短 mode
greedyHaRegx = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegx.search('HaHaHaHaHa')
print(mo1.group())

greedyHaRegx = re.compile(r'(Ha){3,5}?')
mo1 = greedyHaRegx.search('HaHaHaHaHa')
print(mo1.group())
