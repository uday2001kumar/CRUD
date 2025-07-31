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

    def validate_price(self,price):
        if price<0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return price
    
    def validate_stock(self,stock):
        if stock<0:
            raise serializers.ValidationError("Stock must be greater than zero.")
        return stock