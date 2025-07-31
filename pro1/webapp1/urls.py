from django.urls import path
from .views import *
urlpatterns = [
    path('add_category/', add_category),   
    path('list_categories/', get_categories),
    path('add_product/', add_product),
    path('list_products/', get_products),
    path('update_product/<int:pk>/', update_product),
    path('upload_file/', upload_products),
]