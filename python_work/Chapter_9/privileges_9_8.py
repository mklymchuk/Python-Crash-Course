from users_9_3 import Users

class Privileges:
    """Users privileges"""

    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        """Show admin privileges"""
        print("\nAdmin privilages: ")
        for privilege in self.privileges:
            print(privilege)

class Admin(Users):

    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges()