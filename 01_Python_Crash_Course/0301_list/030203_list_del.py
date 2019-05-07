#1. 使用del 语句删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('test')
motorcycles.append('test2')
motorcycles.append('test3')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

#2. 使用方法pop() 删除元素
#方法pop() 可删除列表末尾的元素，并让你能够接着使用它。
popped_motorcycles = motorcycles.pop() 
print(motorcycles)
print(popped_motorcycles)
print(motorcycles.pop())
print(motorcycles.pop())
print(motorcycles)

#使用方法pop()指出最后购买的是哪款摩托车：
motorcycles_buy = ['honda_1', 'yamaha_2', 'suzuki_3']
motorcycles_buylast = motorcycles_buy.pop()
print(motorcycles_buylast)

#3. 弹出列表中任何位置处的元素
motorcycles_any = ['honda_1', 'yamaha_2', 'suzuki_3']
motorcycles_anypop = motorcycles_any.pop(0) 
print("The first one is" + " " + motorcycles_anypop.title() + ".")
print(motorcycles_any)

#4. 根据值删除元素
motorcycles_try_del = ['honda_1', 'yamaha_2', 'suzuki_3']
motorcycles_try_del.remove('suzuki_3') #注意 方法remove() 只删除第一个指定的值。
print(motorcycles_try_del)

#刪除值預先存放在變數當中，需要利用時可再度利用。
motorcycles_try_del_2 = ['honda_1', 'yamaha_2', 'suzuki_3']
too_enpensive = "suzuki_3"
motorcycles_try_del_2.remove(too_enpensive)
print(too_enpensive)
print(motorcycles_try_del_2)