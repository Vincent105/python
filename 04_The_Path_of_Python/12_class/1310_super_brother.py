class Father():
    def __init__(self):
        self.fathermoney = 10000


class Ivan(Father):
    def __init__(self):
        self.ivanmoney = 8000
        super().__init__()


class Ira(Father):
    def __init__(self):
        self.iramoney = 1000
        super().__init__()
    def get_money(self):
        print(self.fathermoney)        
        print(self.iramoney)
        print(Ivan().ivanmoney)        

a = Ira()
a.get_money()

