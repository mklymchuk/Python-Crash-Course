class Employee:
    
    def __init__(self, first_name, last_name, annual_sallary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_sallary = annual_sallary
        
    def give_raise(self):
        self.annual_sallary += 5000