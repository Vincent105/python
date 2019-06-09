class Grandfather():
    def __init__(self):
        self.granfathermoney = 10000
    def get_info(self):
        print("Grandfather's infomation")    

class Father(Grandfather):
    def __init__(self):
        self.fathermoney = 8000
        super().__init__()
    def get_info2(self):        
        print("father's infomation")    

class Son(Father):
    def __init__(self):
        self.son_money = 1000
        super().__init__()
    def get_info3(self):        
        print("son's infomation")    
    def get_money(self):
        print(self.son_money)            
        print("father's infomation:",self.fathermoney)                    
        print("Grandfather's infomation:",self.granfathermoney)                            

vincent = Son()
vincent.get_info3()
vincent.get_info2()
vincent.get_info()
vincent.get_money()
