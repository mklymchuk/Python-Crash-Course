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

class IceCreamStand(Restaurant):
    """An ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_ice_cream_flavors(self):
        """Show to customer a icecream flavors"""
        print("We have the following flavors: ")
        for icecream in self.flavors:
            print(icecream.capitalize())
            
vanila_icecream = IceCreamStand('Baskin Robins', 'icecream', ['vanila', 'chocolate', 'strawberry'])
vanila_icecream.describe_restaurant()
vanila_icecream.show_ice_cream_flavors()