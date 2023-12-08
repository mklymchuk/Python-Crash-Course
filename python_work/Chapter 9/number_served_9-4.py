class Restaurant:
    """A restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Inicialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Restaurant description"""
        print(f"Restaurant {self.restaurant_name} with {self.cuisine_type} cuisines")
        
    def open_restaurant(self):
        """Message if restaurant is open"""
        print(f"Restaurant {self.restaurant_name} is open")
        
    def set_number_served(self, numbers):
        """Set number of served tables"""
        self.number_served = numbers
        
    def increment_number_served(self, numbers):
        """Increment numbers of served tables"""
        self.number_served += numbers
        
        
italian_restaurant = Restaurant('Italiano', 'italian')

print(f"Restaurant {italian_restaurant.restaurant_name}")
print(f"Cuisine {italian_restaurant.cuisine_type}")

italian_restaurant.describe_restaurant()
italian_restaurant.open_restaurant()

restaurant = Restaurant('New rest', 'new food')

restaurant.number_served = 23
print(restaurant.number_served)

restaurant.number_served = 12
print(restaurant.number_served)

restaurant.set_number_served(10)
print(restaurant.number_served)

restaurant.increment_number_served(10)
print(restaurant.number_served)