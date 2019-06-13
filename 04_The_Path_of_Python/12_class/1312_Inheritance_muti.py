class Grandfather():
    '''TEST1'''
    def action1(self):
        '''TEST234'''
        print('Grandfather')


class Father(Grandfather):
    def action2(self):
        print('Father')


class Uncle(Grandfather):
    def action2(self):
        print('Uncle')


class Son(Father, Uncle):
    def action3(self):
        print('son')


a = Son()
a.action1()
a.action2()
a.action3()
print(Grandfather().__doc__)
print(Grandfather().action1.__doc__)
class A():
    def __init__(self):
        print('class A')


class B():
    def __init__(self):
        print('class B')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('class C')
x = C()        

class A():
    def __init__(self):
        super().__init__()
        print('class A')


class B():
    def __init__(self):
        super().__init__()        
        print('class B')


class C(A, B):
    def __init__(self):
        super().__init__()
        print('class C')
x = C() 


 