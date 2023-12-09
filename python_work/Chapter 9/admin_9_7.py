from privileges_9_8 import Privileges

class Users:
    """Class for a making user profile"""
    
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
    
    def describe_user(self):
        """User description"""
        print("The user first name, and last name is: ")
        print(f"{self.first_name.capitalize()} {self.last_name.capitalize()}")
        print(f"User age and gender: {self.age}, {self.sex}")
        
    def greet_user(self):
        """User greeting"""
        print(f"Hello, {self.first_name.capitalize()}\n")

class Admin(Users):

    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges()

admin = Admin('Mykola','Klymchuk', 28, 'male')
admin.describe_user()
admin.privileges.show_privileges()