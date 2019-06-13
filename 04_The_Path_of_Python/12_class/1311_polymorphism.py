class Animals():
    def __init__(self, animal_name):
        self.name = animal_name

    def which(self):
        return 'My pet ' + self.name.title()

    def action(self):
        return ' sleep'


class Dogs(Animals):
    def __init__(self, dog_name):
        super().__init__(dog_name.title())

    def action(self):
        return ' running in the street'


class Monkeys():
    def __init__(self, mockeys_name):
        self.name = 'My monkey ' + mockeys_name.title()

    def which(self):
        return self.name

    def action(self):
        return ' running in the forest'

def doing(obj):
    print(obj.which()," is " + obj.action())

myCat = Animals('lucy')
doing(myCat)
myDog = Dogs('gimi')
doing(myDog)
myMonkeys = Monkeys('taylor')
doing(myMonkeys)
