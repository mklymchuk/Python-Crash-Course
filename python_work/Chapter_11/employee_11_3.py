class Employee:
    
    def __init__(self, first_name, last_name, annual_sallary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_sallary = annual_sallary
        
    def give_raise(self, annual_sallary=0):
        if annual_sallary:
            self.annual_sallary += annual_sallary
        else:
            self.annual_sallary += 5000
        
    def __str__(self):
        return (f"{self.first_name} {self.last_name} {self.annual_sallary}")
        
"""employee = Employee('mykola', 'Klymchuk', 2000)
employee.give_raise()
print(employee)
employee.give_raise(3000)
print(employee)"""