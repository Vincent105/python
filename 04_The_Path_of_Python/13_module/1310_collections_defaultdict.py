from collections import defaultdict

fruits = defaultdict(int)
fruits["apple"] = 20
fruits["orange"]
print(fruits["apple"])
print(fruits["orange"])
print(fruits)

# 用自定義函數重新設計
def price():
    return 10

fruits = defaultdict(price)
fruits["apple"] = 20
fruits["orange"]
print(fruits["apple"])
print(fruits["orange"])
print(fruits)

# 用lambda重新設計
fruits = defaultdict(lambda:10)
fruits["apple"] = 20
fruits["orange"]
print(fruits["apple"])
print(fruits["orange"])
print(fruits)

# 用來設計計數器
fruits = defaultdict(int)
for fruit in ['apple','organge','apple']:
    fruits[fruit] += 1

for fruit,count in fruits.items():
    print(fruit,count)

# 計數器的一般寫法
fruits = {}
for fruit in ['apple','organge','apple']:
    if not fruit in fruits:
        fruits[fruit] = 0
    fruits[fruit] += 1

for fruit,count in fruits.items():
    print(fruit,count)
