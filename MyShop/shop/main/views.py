from django.shortcuts import render, get_object_or_404
from .models import Product
def home(request):
    products = Product.objects.all()  # Отримуємо всі товари
    return render(request, 'main/home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'main/product_detail.html', {'product': product})
def about(request):
    return render(request, 'main/about.html')

def profile(request):
    return render(request, 'main/profile.html')