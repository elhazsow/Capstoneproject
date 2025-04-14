from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Booking(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    no_of_guests = models.IntegerField(default=1)
   

    def __str__(self):
        return f'{self.name} -- {self.no_of_guests} -- {self.date}'
    
class Menu(BaseModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    inventory = models.IntegerField(default = 0)
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    

    