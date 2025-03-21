from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.IntegerField(5, primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    time = models.TimeField()
    no_of_guests = models.IntegerField(6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    id = models.IntegerField(5, primary_key=True)
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    inventory = models.IntegerField(5)
    created_at = models.DateTimeField(auto_now_add = True)
    
    
    
    def __str__(self):
        return self.title, self.price, self.description, self.inventory