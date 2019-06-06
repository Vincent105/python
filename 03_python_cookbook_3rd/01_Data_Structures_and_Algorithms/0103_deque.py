#保留最後 N 個元素

from collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open('03_python_cookbook_3rd\\01_Data_Structures_and_Algorithms\\somefile.txt','r') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

#deque(maxlen=N) 構造函數會新建一個固定大小的隊列。當新的元素加入並且這個隊列已滿的時候， 最老的元素會自動被移除掉。
q = deque(maxlen=3)

q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

#deque 類可以被用在任何你只需要一個簡單隊列數據結構的場合。 如果你不設置最大隊列大小，那麼就會得到一個無限大小隊列
#可以在隊列的兩端執行添加和彈出元素的操作。
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)

