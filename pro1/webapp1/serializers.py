from rest_framework import serializers
from .models import Category, Products
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    category_name= serializers.CharField(source='category.category_name', read_only=True)
    class Meta:
        model = Products
        fields = ['product_id', 'product_name', 'category','category_name', 'price', 'stock']