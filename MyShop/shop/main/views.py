from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
def home(request):
    products = Product.objects.all()  # Отримуємо всі товари
    return render(request, 'main/home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'main/product_detail.html', {'product': product})
def about(request):
    return render(request, 'main/about.html')


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'main/profile.html', {'form': form})
