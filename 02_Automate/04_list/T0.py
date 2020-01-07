import copy

spam_0 = [2,4,6,8,10]

spam_1 = copy.copy(spam_0)

spam_1[2] = 'hello'
print(spam_1)

spam_2 = ['a','b','c','d']
# print(spam_2[int(print'3'*2)/11])
print(spam_2[-1])
print(spam_2[:2])

bacon = [3.14, 'cat', 11, 'cat', True]
print(bacon.index('cat'))
bacon.append(99)
print(bacon)
bacon.remove('cat')
print(bacon)
