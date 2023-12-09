class Privileges:
    """Users privileges"""

    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        """Show admin privileges"""
        print("\nAdmin privilages: ")
        for privilege in self.privileges:
            print(privilege)