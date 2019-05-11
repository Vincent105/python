print(round(1.5))
print(round(2.5))
print(round(2.150,1))
x = 97
print(chr(x))

string = 'abc'
print(len(string))

stringBytes = string.encode('utf-8')
print(len(stringBytes))
print(type(stringBytes))
print(stringBytes)


name = '王晏宗'
print(len(name))

nameBytes = name.encode('utf-8')
print(len(nameBytes))
print(type(nameBytes))
print(nameBytes)

stringUcode = stringBytes.decode('utf-8') 
print(len(stringUcode))
print(type(stringUcode))
print(stringUcode)

nameUcode = nameBytes.decode('utf-8') 
print(len(nameUcode))
print(type(nameUcode))
print(nameUcode)


