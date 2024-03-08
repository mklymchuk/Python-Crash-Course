from django.db import models

class Pizza(models.Model):
    """A pizza to create."""
    name = models.CharField(max_length=50)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.name

class Topping(models.Model):
    """Pizza toppings."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    
    def __str__(self):
        """Returning a string representation of the model."""
        return f"{self.name[:50]}"