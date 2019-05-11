# ex13_5.py
import random                       # 導入模組random

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
print("執行前串列 : ", fruits)
for i in range(len(fruits)):
    fruit = random.choice(fruits)
    print("刪除 : ", fruit)
    fruits.remove(fruit)
    print("目前串列 : ", fruits)





