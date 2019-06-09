class Animals():
    def __init__(self, animal_name, animal_age):
        self.name = animal_name
        self.age = animal_age

    def run(self):
        print(self.name.title(), "is running.")


class Dogs(Animals):
    def __init__(self, dog_name, dog_age):
        super().__init__('My pet' + dog_name.title() , dog_age)
    def sleeping(self):
        print(self.name.title(), "is sleeping.")    


mycat = Animals('d',21)
print(mycat.name.title(),mycat.age)
mycat.run()

mydog = Dogs('e',3)
print(mydog.name,mydog.age)
mydog.run()
mydog.sleeping()