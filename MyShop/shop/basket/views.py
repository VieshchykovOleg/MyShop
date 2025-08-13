from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .models import BasketItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
@login_required
def basket(request):
    items = BasketItem.objects.filter(user=request.user)
    return render(request, 'basket/basket.html', {'items': items})

@login_required
def add_to_basket(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    basket_item, created = BasketItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        basket_item.quantity += 1
        basket_item.save()
    return redirect('basket')


def cart_update(request, item_id):
    item = get_object_or_404(BasketItem, id=item_id)
    action = request.POST.get('action')

    if action == 'increase':
        item.quantity += 1
    elif action == 'decrease' and item.quantity > 1:
        item.quantity -= 1
    item.save()

    return JsonResponse({
        'quantity': item.quantity
    })

def cart_remove(request, item_id):
    item = get_object_or_404(BasketItem, id=item_id)
    item.delete()
    return JsonResponse({'removed': True})

@login_required
def checkout(request):
    items = BasketItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in items)
    return render(request, 'basket/checkout.html', {'items': items, 'total': total})