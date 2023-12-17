import unittest
from python_work.Chapter_11.employee_11_3 import Employee

class TestEmployeeRaise(unittest.TestCase):
    """Test employee salary raise"""
    
    def setUp(self):
        """Create a empoyee and set of raise salary"""
        self.test_employee = Employee('mykola', 'klymchuk', 1000)
        return super().setUp()
        
    def test_give_default_raise(self):
        """Raise sallary for 5000$ by default"""
        self.test_employee.give_raise()
        
    def test_give_custom_raise(self):
        """Raise sallary for custom ammount"""
        self.test_employee.give_raise(2000)
        
    if __name__ == '__main__':
        unittest.main()