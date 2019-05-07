#字典 是一系列键—值对 。每个键 都与一个值相关联，你可以使用键来访问与之相关联的值。
alien_0 ={}
alien_1 ={}
alien_0 = {'color': 'green','point': 5,'list': ['1','2']}
alien_1 = {'color': 'red','point': 10,'list': ['1','2']}

print(alien_0['color'])
print(alien_0['point'])
print(alien_0['list'])

new_point = alien_0['point']
print("You just earn " + str(new_point) + " points")

new_point = alien_1['point']
print("You just earn " + str(new_point) + " points")

#字典元素新增
alien_0['x_place'] = 100
alien_0['y_place'] = 55

print(alien_0)

#字典元素修改
alien_0['color'] = 'yellow'
print(alien_0)

#字典範例:移動位置
alien_3 = {'x_position': 30, 'y_posiotion': 25, 'speed': 'medium'}
print("Orginal x-position: " + str(alien_3['x_position']))

if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_3['x_position'] = alien_3['x_position'] + x_increment
print("New position " + str(alien_3['x_position']))   

alien_3['z_position'] = 100 
print(alien_3)  

#同时删除键相关联的值。
del alien_3['z_position']		
print(alien_3)  

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edard': 'c#',
	'phil': 'python',
}

print("Jen's favorite languages is " + favorite_languages['jen'].title() + '.')