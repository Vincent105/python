cars = ['toyota', 'nissan', 'honda', 'nissan']
search_str = 'nissan'
i = cars.index(search_str)
print(i)

num1 = cars.count(search_str)
print('所搜尋的元素%s出現%d次'%(search_str,num1))

nums = [7, 12, 30, 12, 30, 9, 8]
num2 = nums.count(30)
search_val = 30
print('所搜尋的元素%s出現%d次'%(search_val,num2))
