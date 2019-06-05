def modifySong(songstr):
    for ch in songstr:
        if ch in ".,?":
            songstr = songstr.replace(ch, '')
    return songstr

def wordCount(songcount):
    global mydict
    songlist = songcount.split()
    print(songlist)
    mydict = {wd: songlist.count(wd) for wd in songlist}


data = """Are you sleeping? Are you sleeping? Brother John, Brother John? Morning bells are ringing. 
Morning bells are ringing. Ding, dong, ding. Ding, dong, ding."""

mydict = {}
song = modifySong(data.lower())  
print(song)
wordCount(song)
print(mydict)

