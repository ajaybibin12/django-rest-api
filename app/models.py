from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name