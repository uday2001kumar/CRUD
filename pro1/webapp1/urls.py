from django.urls import path
from .views import *
urlpatterns = [
    path('add_category/', add_category),   
    path('get_categories/', get_categories),
    path('add_product/', add_product),
    path('get_products/', get_products),
    path('update_product/<int:pk>/', update_product),
    path('upload_products/', upload_products),
]