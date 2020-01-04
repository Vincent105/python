# 實現一個優先級隊列
import heapq


class PiorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q = PiorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

# 第一個 pop() 返回優先級最高的元素。 如果兩個有相同優先級的元素，pop 操作按照它們插入隊列的順序返回。
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
