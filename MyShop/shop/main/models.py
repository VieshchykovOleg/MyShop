from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва товару")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to='main/img/products/', blank=True, null=True, verbose_name="Фото")
    description = models.TextField(verbose_name="Опис")

    def __str__(self):
        return self.title

class BasketItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.title} x {self.quantity} для {self.user.username}"



