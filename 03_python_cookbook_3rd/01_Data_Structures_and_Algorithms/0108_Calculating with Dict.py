# 字典的運算
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))  # 使用 zip() 函數將鍵和值反轉
max_price = max(zip(prices.values(), prices.keys()))
sorted_price = sorted(zip(prices.values(), prices.keys()))
print(min_price)
print(max_price)
print(sorted_price)

# 透過其他方法取值
print(min(prices.values()))
print(max(prices.values()))

# 透過lambda取得key值 最大最小
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_value)
max_value = prices[max(prices, key=lambda k: prices[k])]
print(max_value)

# 注意使用到了 (值，鍵) 對。當多個實體擁有相同的值的時候，鍵會決定返回結果。 比如，在執行 min() 和 max() 操作的時候，
# 如果恰巧最小或最大值有重複的，那麼擁有最小或最大鍵的實體會返回：
prices = {'AAA': 45.23, 'ZZZ': 45.23}
min_a = min(zip(prices.values(),prices.keys()))
print(min_a)
max_a = max(zip(prices.values(),prices.keys()))
print(max_a)
