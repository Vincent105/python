mysports = ['a', 'b']
friendsports = mysports[:]

print(id(friendsports))
print(id(mysports))

mysports.append(1)
friendsports.append(2)

print(friendsports)
print(mysports)

a = [1, 2, 3, [4, 5, 6]]
b = a.copy()
a.append(7)
print(a)
print(b)
a[3].append(7)
print(a)
print(b)

import copy

a = [1, 2, 3, [4, 5, 6]]
b = copy.deepcopy(a)
a.append(10)
a[3].append(11)
print(a)
print(b)
