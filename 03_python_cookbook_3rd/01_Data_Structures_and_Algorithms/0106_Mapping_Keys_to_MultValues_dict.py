# 字典中的鍵映射多個值

from collections import defaultdict

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

defaultDict = defaultdict(list)
defaultDict['a'].append(1)
defaultDict['a'].append(2)
defaultDict['a'].append(3)
defaultDict['b'].append(4)
defaultDict['b'].append(5)


defaultSet = defaultdict(set)
defaultSet['a'].add(1)
defaultSet['a'].add(2)
defaultSet['a'].add(3)
defaultSet['b'].add(4)
defaultSet['b'].add(5)

print(defaultDict)
print(defaultSet)

# 可以在一個普通的字典上使用 setdefault() 方法來代替
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('a', []).append(3)
d.setdefault('b', []).append(4)
d.setdefault('b', []).append(5)
print(d)
