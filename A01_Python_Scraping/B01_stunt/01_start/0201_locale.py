# coding: UTF-8
# author: Vincent Wang

import sys
import locale
from bs4 import UnicodeDammit

def p(f):
    print('%s.%s():%s'%(f.__module__ , f.__name__, f())) 

#返回系統使用預設編碼
p(sys.getdefaultencoding)

#返回轉換unicode文件至系統文件所使用的編碼
p(sys.getfilesystemencoding)

#返回預設區域語言及編碼
p(locale.getdefaultlocale)

#返回用戶端文件預設編碼
p(locale.getpreferredencoding)

dammit = UnicodeDammit(u"\u4e2d\u56fd\u5c06")
print(dammit)    
print(dammit.unicode_markup)    

dammit = UnicodeDammit("Sacr \xe9 bleu!")
print(dammit.unicode_markup)        
print(dammit.original_encoding)