from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from .models import Category, Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    category = SerializerMethodField('category_data')

    def category_data(self, product: Product):
        return CategorySerializer(product.category).data

    class Meta:
        model = Product
        fields = "__all__"
