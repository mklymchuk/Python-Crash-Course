from django.db import models

# Create your models here.
class Pizza(models.Model):
    """A pizza to create."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)