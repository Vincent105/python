val = None
if val:
    print('I love Java')
else:
    print('I love Python')

def is_none(string,x):
    if x is None:
        print("%s=None"%string)
    elif x:
        print("%s=Ture"%string)    
    else:
        print("%s=False"%string)                    

is_none('空串列',[])
is_none('空元祖',())
is_none('空字典',{})
is_none('空集合',set())
is_none('None',None)
is_none('True',True)
is_none('False',False)





