spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat') #如果该值在列表中出现多次，只有第一次出现的值会被删除。
print(spam)
