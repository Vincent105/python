import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42

print(spam)
print(cheese)

#copy 和 deepcopy 不同之處在於 copy 儘會複製當前物件而 deepcopy 則是若該物件有屬性指向其他物件，則也會一併複製
# 範例:
