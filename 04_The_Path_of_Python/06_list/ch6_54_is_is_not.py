x = 10
y = 10
z = 15
r = z - 5

boolean_value = x is y
print('x位置=%d,y位置=%d'%(id(x),id(y)))
print('x=%d,y=%d boolean:%d'%(x,y,boolean_value))

boolean_value = x is z
print('x位置=%d,z位置=%d'%(id(x),id(z)))
print('x=%d,z=%d boolean:%d'%(x,z,boolean_value))

boolean_value = x is not r
print('x位置=%d,r位置=%d'%(id(x),id(r)))
print('x=%d,r%d boolean:%d'%(x,r,boolean_value))
 