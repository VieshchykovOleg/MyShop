from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.db.models import Q
from django.db.models import Avg

def home(request):
    products = Product.objects.all()

    query = request.GET.get("q")
    if query:
        products = products.filter(Q(title__icontains=query) | Q(description__icontains=query))

    sort = request.GET.get("sort")
    if sort == "price_asc":
        products = products.order_by("price")
    elif sort == "price_desc":
        products = products.order_by("-price")
    elif sort == "rating_desc":
        products = products.annotate(avg_rating=Avg("comments__rating")).order_by("-avg_rating")

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
