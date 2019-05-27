#intersection
math = {'a','b','c'}
physic = {'d','b','e'}
both = math & physic
print(both)

#union
math = {'a','b','c'}
physic = {'d','b','e'}
both = math | physic
print(both)

#diff
math = {'a','b','c'}
physic = {'d','b','e'}
both = math - physic
print(both)
both = math.difference(physic)
print(both)

#symmetric diff
math = {'a','b','c'}
physic = {'d','b','e'}
both = math ^ physic
print(both)
both = math.symmetric_difference(physic)
print(both)