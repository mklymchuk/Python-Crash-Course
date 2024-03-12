from django.db import models

class Meal(models.Model):
    """A meal description."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text

class MealPlan(models.Model):
    """Something specific about a meal."""
    meal_description = models.ForeignKey(Meal, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Meal plans'
   
    def __str__(self):
        """Return a string representation of the model."""
        return f"Meal plan: {self.text[:50]}"
