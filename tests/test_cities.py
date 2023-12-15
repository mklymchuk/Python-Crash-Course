import unittest
from python_work.Chapter_11.city_function import city_country

class CityCountryTestCase(unittest.TestCase):
    """Test correct output of city country"""
    
    def test_city_country(self):
        """Test correct output"""
        city_country_test = city_country('santiago', 'chili')
        self.assertEqual(city_country_test, 'Santiago, Chili')
        
    def test_city_country_population(self):
        """Test correct population output"""
        city_country_test = city_country('santiago', 'chili', '5000000')
        self.assertEqual(city_country_test, 'Santiago, Chili - Population 5000000')
        
    if __name__ == '__main__':
        unittest.main()