from collections import deque


def palinrome(word):
    wd = deque(word)
    while len(wd) > 1:
        if wd.pop() != wd.popleft():
            return False
    return True

def palinrome2(word):
    return word == word [::-1]

print(palinrome('x'))
print(palinrome('abcba'))            
print(palinrome('python'))        
