from django.contrib import admin
from .models import Product
from .models import BasketItem

admin.site.register(Product)
admin.site.register(BasketItem)