# ex12_9.py
class Grandfather():
    """ 定義祖父的資產 """
    def __init__(self):
        super().__init__()
        self.grandfathermoney = 10000
    def get_info1(self):
        print("Grandfather's information")

class Grandmother():
    """ 定義祖母的資產 """
    def __init__(self):
        super().__init__()
        self.grandmothermoney = 20000   
    def get_info4(self):
        print("Grandmother's information")
        
class Father(Grandfather,Grandmother):  # 父類別是Grandfather/Grandmother
    """ 定義父親的資產 """
    def __init__(self):
        super().__init__()
        self.fathermoney = 8000        
    def get_info2(self):
        print("Father's information")

class Ivan(Father):             # 父類別是Father
    """ 定義Ivan的資產 """
    def __init__(self):
        super().__init__()
        self.ivanmoney = 3000        
    def get_info3(self):
        print("Ivan's information")
    def get_money(self):        # 取得資產明細
        print("\nIvan資產: ", self.ivanmoney,
              "\n父親資產: ", self.fathermoney,
              "\n祖父資產: ", self.grandfathermoney,
              "\n祖母資產: ", self.grandmothermoney)
        
ivan = Ivan()
ivan.get_info3()                # 從Ivan中獲得
ivan.get_info2()                # 流程 Ivan -> Father
ivan.get_info1()                # 流程 Ivan -> Father -> Grandfather
ivan.get_info4()                # 流程 Ivan -> Father -> Grandmother
ivan.get_money()                # 取得資產明細
