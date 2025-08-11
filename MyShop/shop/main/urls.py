from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('basket/', views.basket, name='basket'),
    path('basket/add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('cart/update/<int:item_id>/', views.cart_update, name='cart_update'),
    path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('checkout/', views.checkout, name='checkout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)