from django.urls import path
from . import views 

urlpatterns = [
 
path('', views.product_list, name='product_list'),
path('product/', views.product, name='product'),
path('search/', views.search, name='search'),




]
