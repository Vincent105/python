# ex12_3.py
class Myschool():
    def __init__(self,name,score):
        self.name = name
        self.score = score
        self.schoolname = "Python School"
    def msg(self):
        print(self.schoolname)
        print("Hi!" + self.name.title() + "你的成績是" + str(self.score) + "分")

A = Myschool("kevin",80)
A.msg()



