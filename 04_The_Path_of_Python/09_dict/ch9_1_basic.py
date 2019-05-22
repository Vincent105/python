fruits = {'watermelon':10, 'mango':20, 'banana':30}
noodles = {'拉麵':100, '涼麵':80, '牛肉麵':150}

print(fruits)
print(noodles)
print('資料型別是',type(noodles))
print('芒果一公斤價錢:',fruits['mango'])
print('牛肉麵一碗價錢:',noodles['牛肉麵'])

#增加字典元素
fruits['apple'] = 300
print(fruits)

#修改字典元素
fruits['apple'] = 150
print(fruits)

#刪除字典元素
del fruits['apple']
print(fruits)

#使用pop()移除字典元素
objKey = 'watermelon'
del_value = fruits.pop(objKey)
print('目前的水果是:', fruits)
print('移除的水果是:%s價錢是%d'%(objKey,del_value))

#使用popitem()隨機移除字典元素
ran_value = fruits.popitem()
print('目前的水果是:', fruits)
print('隨機移除水果:', ran_value)

#使用clear()清除字典              
fruits = {'watermelon':10, 'mango':20, 'banana':30}
print(fruits)
fruits.clear()
print(fruits)

#使用整個字典
del fruits

#建立空白字典
soldier0 = {}
soldier0['tag'] = 'red'
soldier0['score'] = 10 
print('設定小兵屬性：',soldier0)

#拷貝字典shallow copy
fruits = {'watermelon':10, 'mango':20, 'banana':30}
copy_fruits = fruits.copy()
print(id(fruits),fruits)
print(id(copy_fruits),copy_fruits)

#拷貝字典deep copy
import copy
a ={'a':[1, 2, 3]}
b = copy.deepcopy(a)
print(a,b)
b['a'].append(4)
print(a,b)

#取得字典數量
fruits = {'watermelon':10, 'mango':20, 'banana':30}
print(len(fruits))

#合併字典
fruits_a = {'watermelon':10, 'mango':20, 'banana':30}
fruits_b = {'watermelon_bb':10, 'mango_bb':20, 'banana':20}
fruits_a.update(fruits_b)
print(fruits_a)

#zip
mydict = dict(zip('abcde',range(5)))
print(mydict)

#確認key是否存在字典
fruits = {'watermelon':10, 'mango':20, 'banana':30}
key = input('請輸入key值：')
value = input('請輸入value值：')
if key in fruits:
    print('%s存在'%key)
else:
    fruits[key] = value
    print('目前字典內容：',fruits)




