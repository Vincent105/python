song = "Are you sleeping? Are you sleeping? Brother John, Brother John? Morning bells are ringing. \
Morning bells are ringing. Ding, dong, ding. Ding, dong, ding."

print("原始文章:")
print(song)

songlower = song.lower()
print("轉換小寫:")
print(songlower)

#去符號
for ch in songlower:
    if ch in "?":
        songlower = songlower.replace(ch,"")
    elif ch in ".":
        songlower = songlower.replace(ch,"")        
    elif ch in ",":
        songlower = songlower.replace(ch,"")                
print(songlower)

songlist = songlower.split()
print(songlist)

mydict = {wd:songlist.count(wd) for wd in songlist}
print(mydict)        
'''
mydict = {}

for wd in songlist:
    if wd in mydict:
        mydict[wd] += 1
    else:        
        mydict[wd] = 1

print(mydict)        
'''