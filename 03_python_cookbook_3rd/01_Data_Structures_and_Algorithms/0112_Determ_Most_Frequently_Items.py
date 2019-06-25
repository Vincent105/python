from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(word_counts)
print(top_three)

print("一個 Counter 對象就是一個字典，將元素映射到它出現的次數上")
print(word_counts['look'])

print("手動增加計數，可以簡單的用加法")
morewords = ['why','are','you','not','looking','in','my','eyes','eyes','in']
word_count_1 = {}
for word in morewords:
    if word not in word_count_1:
        word_count_1[word] = 0
    word_count_1[word] += 1
print(word_count_1)

print("你可以使用 update() 方法：")
word_counts.update(morewords)
print(word_counts)

print("Counter 實例一個鮮為人知的特性是它們可以很容易的跟數學運算操作相結合")
a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
# Combine counts
c = a + b
print(c)

# Subtract counts
c = a - b
print(c)