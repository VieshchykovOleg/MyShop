from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва товару")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    image = models.ImageField(upload_to='main/img/products/', blank=True, null=True, verbose_name="Фото")
    description = models.TextField(verbose_name="Опис")

    def __str__(self):
        return self.title




