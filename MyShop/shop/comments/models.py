from django.db import models
from django.contrib.auth.models import User
from main.models import Product


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст коментаря")
    rating = models.PositiveSmallIntegerField(verbose_name="Оцінка", choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Коментар від {self.user.username} для {self.product.title}"

    class Meta:
        ordering = ['-created_at']
