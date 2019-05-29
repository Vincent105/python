students = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
math = {'a','b','c'}
physics = {'c','d','e'}
math_ph = math&physics
unattend = students- (math|physics)
print('有%d人參加兩個營隊:'%len(math_ph),math_ph)
print(unattend)

#集合生成式
A = {n for n  in range(1,100,2)}
print(A)

A = {n for n  in range(1,100,2) if n%11 ==0}
print(A)
