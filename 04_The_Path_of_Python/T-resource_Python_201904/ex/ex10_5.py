# ch10_5.py
song = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()                    # 歌曲改為小寫

# 將歌曲的標點符號用空字元取代
for ch in songLower:                
    if ch in ".,?!-*":
        songLower = songLower.replace(ch,'')

# 將歌曲字串轉成串列
songList = songLower.split()        

# 將歌曲串列處理成字典 
mydict = {wd:songList.count(wd) for wd in set(songList)}
# 排序
newList = sorted(mydict.items(),key=lambda item:item[1])

newDict = dict(newList)                     # 將串列轉成字典
for wd, count in newDict.items():
    print(wd, ":", count)                 









