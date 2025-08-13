from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket, name='basket'),
    path('add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('update/<int:item_id>/', views.cart_update, name='cart_update'),
    path('remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('checkout/', views.checkout, name='checkout'),
]
