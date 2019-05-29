#add()
cities = {'Taipei', 'Bejiing', 'Tokyo'}
cities.add('Chicago')

#copy()
numset = {1, 2, 3}
deep_numset = numset
deep_numset.add(10)
print(numset)
print(deep_numset)

shallow_numset = numset.copy()
shallow_numset.add(10)
print(numset)
print(shallow_numset)

#remove()
cities = {'Taipei', 'Bejiing', 'Tokyo'}
cities.remove('Taipei')
print(cities)

#discard()
cities = {'Taipei', 'Bejiing', 'Tokyo'}
cities.discard('pig')
print(cities)

#pop()
cities = {'Taipei', 'Bejiing', 'Tokyo'}
cities.pop()
print(cities)

#clear()
cities = {'Taipei', 'Bejiing', 'Tokyo'}
cities.clear()
print(cities)

#isdisjoint()
A = {'a', 'b', 'c'}
B = {'c', 'd', 'e'}
C = {'h', 'k', 'p'}

boolean = A.isdisjoint(B)
print(boolean)
boolean = A.isdisjoint(C)
print(boolean)

#issubset()
A = {'a', 'b', 'c'}
B = {'a', 'b', 'c', 'd', 'e', 'f'}
C = {'k', 'm', 'n'}
boolean = A.issubset(B)
print(boolean)
boolean = A.issubset(C)
print(boolean)

#issuperset()
A = {'a', 'b', 'c', 'd', 'e', 'f'}
B = {'a', 'b', 'c'}
C = {'k', 'm', 'n'}
boolean = A.issuperset(B)
print(boolean)
boolean = A.issuperset(C)
print(boolean)

#intersection_update()
A = {'a', 'b', 'c', 'd'}
B = {'a', 'k', 'c'}
C = {'c', 'f', 'w'}
ret_value = A.intersection_update(B)
print(A)
print(B)
ret_value = A.intersection_update(C)
print(A)
print(C)

#update()
A = {'a', 'b', 'c', 'd'}
B = {'a', 'k', 'c'}
C = {'c', 'f', 'w'}
ret_value = A.update(B)
print(A)
print(B)
ret_value = A.update(C)
print(A)
print(C)

#difference_update()
A = {'a', 'b', 'c', 'd'}
B = {'a', 'k', 'c'}
C = {'c', 'f', 'w'}
ret_value = A.difference_update(B)
print(A)
print(B)
ret_value = A.difference_update(C)
print(A)
print(C)

#symmetric_difference_update()
A = {'a', 'b', 'c', 'd'}
B = {'a', 'k', 'c'}
ret_value = A.symmetric_difference_update(B)
print(A)
print(B) 