from django.urls import path
from .views import *

urlpatterns = [

    path('manufacturers/', getManufacturers, name="all_manufacturer"),
    path('manufacturers/<str:pk>/', getManufacturer, name="manufacturer"),

    path('categories/', getCategories, name='getCategories'),
    
    path('products/', getProducts, name="all_products"),
    path('products/<str:pk>/', getProduct, name="product"),
]