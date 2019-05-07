class User():
    '''使用者登入'''
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print('Login-in user is ' + self.first_name.title() + ' ' + self.last_name.title())

    def greet_user(self):
        print('Hello ' + self.first_name.title() + ' ' + self.last_name.title())    

    def read_login_attemps(self):
        print('The user ' + self.first_name.title() + "'s login times is " + str(self.login_attempts))

    def increment_login_attempts(self,increse_value):
        login_attempts += increse_value

    def reset_login_attempts(self,reset_value):
        self.login_attempts = reset_value
        print('the number is ' +  str(self.login_attempts))

first_name = input('Please type your first name:')
last_name = input('Please type your last name:')
my_user = User(first_name,last_name)
my_user.describe_user()
my_user.greet_user()
my_user.read_login_attemps()
my_user.reset_login_attempts(0)