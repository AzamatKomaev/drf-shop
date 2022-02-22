from django.urls import path

from . import views


urlpatterns = [
    path('categories/', views.CategoryViewSet.as_view({'get': 'list'}), name='category.list'),
    path('categories/<int:pk>', views.CategoryViewSet.as_view({'get': 'retrieve'}), name='category.detail'),
]
