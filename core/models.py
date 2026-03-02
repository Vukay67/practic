from django.db import models

PRODUCT_CATEGORY_CHOICES = [
    ['Компьютерная техника', 'Компьютерная техника'],
    ['Мобильная техника', 'Мобильная техника'],
    ['Аудио и видео', 'Аудио и видео'],
    ['Игровая техника', 'Игровая техника'],
    ['Бытовая техника', 'Бытовая техника'],
    ['Умные устройства', 'Умные устройства'],
    ['Фото и видео', 'Фото и видео'],
    ['Сетевое оборудование', 'Сетевое оборудование'],
    ['Аксессуары', 'Аксессуары'],
]

class Product(models.Model):
    name = models.CharField()
    description = models.TextField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/")
    category = models.CharField(
        choices=PRODUCT_CATEGORY_CHOICES
    )

    def __str__(self):
        return f"{self.name} - {self.price} $"
    
