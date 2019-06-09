class Counter():
    counter = 0
    def __init__(self):
        Counter.counter += 1
    @classmethod
    def show_counter(cls):
        print('class method')        
        print('counter = ',cls.counter)
        print('counter = ',Counter.counter)

one = Counter()
two = Counter()
three = Counter()
Counter.show_counter()