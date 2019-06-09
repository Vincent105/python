class Score():
    def __init__(self, score):
        self.__score = score

    def getscore(self):
        print('inside the get score')
        return self.__score

    def setscore(self, score):
        print('inside the get score')
        self.__score = score
    sc = property(getscore, setscore)


stu = Score(50)
print(stu._Score__score)

stu = Score(150)
print(stu._Score__score)

stu.setscore(1000)
print(stu.getscore())

print(stu.sc)
stu.sc = 5000
print(stu.sc)