class Users:
    """Class for a making user profile"""
    
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0
    
    def describe_user(self):
        """User description"""
        print("The user first name, and last name is: ")
        print(f"{self.first_name.capitalize()} {self.last_name.capitalize()}")
        print(f"User age and gender: {self.age}, {self.sex}")
        print(f"User login attempt: {self.login_attempts}")
        
    def greet_user(self):
        """User greeting"""
        print(f"Hello, {self.first_name.capitalize()}\n")

    def increment_login_attempts(self):
        """Increment loggin attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        
mykola_1994 = Users('mykola', 'klymchuk', 28, 'male')
dima_1996 = Users('dmytro', 'klymchuk', 27, 'male')
vika_2007 = Users('victoria', 'klymchuk', 16, 'female')

mykola_1994.increment_login_attempts()
mykola_1994.describe_user()
mykola_1994.greet_user()

dima_1996.describe_user()
dima_1996.greet_user()

vika_2007.describe_user()
vika_2007.greet_user()

mykola_1994.increment_login_attempts()
mykola_1994.increment_login_attempts()
mykola_1994.describe_user()

print("\n")

mykola_1994.reset_login_attempts()
mykola_1994.describe_user()