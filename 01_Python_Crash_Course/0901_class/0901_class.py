class Dog():
    """模擬小狗動作的簡單嘗試"""
    def __init__(self, name, age):
        #初始化屬性
        self.name = name
        self.age = age

    def sit(self):
        #模擬命令蹲下
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        #模擬打滾
        print(self.name.title() + ' roll over.')

my_dog = Dog('willie', 10)
your_dog =Dog('vincent', 2)

print('My dog is ' + my_dog.name.title())
print('My dog is ' + str(my_dog.age) + ' years old.') 

my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()
