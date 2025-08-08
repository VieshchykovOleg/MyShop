from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)