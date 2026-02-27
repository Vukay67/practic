from django.db import models

class Product(models.Model):
    name = models.CharField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return f"{self.name} - {self.price} $"
