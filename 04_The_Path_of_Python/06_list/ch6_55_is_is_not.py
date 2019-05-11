my_sports = ['basketball','baseball']
sports1 = my_sports         #賦值
sports2 = my_sports[:]      #切片拷貝新串列

print('我喜歡的運動是：',my_sports,'位置是',id(my_sports))
print('我喜歡的運動(1)：',sports1,'位置是',id(sports1))
print('我喜歡的運動(2)：',sports2,'位置是',id(sports2))

boolean_value = my_sports is sports1
print(boolean_value)

boolean_value = my_sports is sports2
print(boolean_value)

boolean_value = my_sports is not sports1
print(boolean_value)

boolean_value = my_sports is not sports2
print(boolean_value)

boolean_value = sports1 is sports2
print(boolean_value)

x = []
if x is None:
    print('x is None')
else:
    print('x is not None')        
    