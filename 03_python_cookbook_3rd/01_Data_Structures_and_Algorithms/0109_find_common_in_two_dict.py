# 查找兩字典的相同點
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

#簡單的集合比對
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c)

d = {key:b[key] for key in b.keys() - {'x','y'}}
print(d)
