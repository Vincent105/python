print([1,2,3])
print(['cat', 'bat', 'rat', 'elephant'])
print(['hello', 3.1415, True, None, 42])

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)

print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])
print('Hello ' + spam[0])
print('Hello ' + spam[int(1.0)])

#負數
print(spam[-1])
print(spam[-2])

#切片
print(spam[1:3])
print(spam[:3])
print(spam[2:])
print(spam[:])

#列表包含列表
spam = [['cat', 'bat'],[1,2,3]]
print(spam[0])
print(spam[1])

#透過len取得列表函數
print(len(spam))

#列表值修改
spam[0] = 'aaakt'
print(spam[:])

spam[1] = spam[0]
print(spam)

#列表值連接
print([1,2,3] + ['A','B','C'])
print(['A','B','C']*3)
spam = [1,2,3]
spam = spam + ['A','B','C']
print(spam)

#列表值刪除
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
