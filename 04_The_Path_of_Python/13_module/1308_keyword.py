import keyword

print(keyword.kwlist)

keywordlist = ['true', 'as', 'break', 'sse']
for x in keywordlist:
    print("%8s" % x, keyword.iskeyword(x))
