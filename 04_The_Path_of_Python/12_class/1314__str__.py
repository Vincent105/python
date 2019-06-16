#協助返回容易讀取的字串
class Name:
    def __init__(self, name):
        self.name = name
    def __str__(self):          
        return '%s'% self.name        
    __repr__ = __str__        


a = Name('huang')
print(a)
