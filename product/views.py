from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ViewSet):

    def list(self, request: Request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request, pk: int):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
