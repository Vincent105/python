# ex6_9.py
song = '''Are you sleeping are you sleeping Brother John Brother John
Morning bells are ringing morning bells are ringing
Ding ding dong Ding ding dong'''
print("歌曲字串內容")
print(song)

newsong = song.lower()                      # 將所有字串轉成小寫
songlist = newsong.split()
print("歌曲串列內容")
print(songlist)
print("歌曲的字數 : %d" % len(songlist))

msg = input("請輸入字串 : ")
num = songlist.count(msg)
print("%s 出現的 %d 次 " % (msg, num))





