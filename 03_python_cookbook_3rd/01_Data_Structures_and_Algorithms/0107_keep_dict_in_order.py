from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key,d[key])

json.dumps(d)

#一個 OrderedDict 的大小是一個普通字典的兩倍，因為它內部維護著另外一個鏈表。 所以如果你要構建一個需要大量 OrderedDict 實例的數據結構的時候
#（比如讀取 100,000 行 CSV 數據到一個 OrderedDict 列表中去）， 那麼你就得仔細權衡一下是否使用 OrderedDict 帶來的好處要大過額外內存消耗的影響。