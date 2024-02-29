import unittest
from python_repos import status_code_response

class StatusCodeTest(unittest.TestCase):
    """Test for the status code."""
    
    def test_status_code(self):
        """Test if status code returned is 200."""
        check_status_code = status_code_response()
        self.assertEqual(check_status_code, 200)
        
if __name__ == '__main__':
    unittest.main()