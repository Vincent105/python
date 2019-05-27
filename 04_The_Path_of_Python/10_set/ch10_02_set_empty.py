empty_dict = {}
print(empty_dict)
print(type(empty_dict))

empty_dict = set()
print(empty_dict)
print(type(empty_dict))

x = set('Deepstone')
print(x)
print(type(x))

fruits = ['a','b','c','a']
x = set(fruits)
print(x)

y = set(['a','b','c','a'])
print(y)

y = set(('a','b','c','a'))
print(y)

fruits = {
    'a':1,
    'b':2,
    'a':3,
    }
x = set(fruits)
print(x)