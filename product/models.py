from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField('name', max_length=255)
    description = models.TextField('description')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField('name', max_length=255)
    description = models.TextField('description')
    price = models.FloatField('price')
    parameters = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    photos = models.ManyToManyField('ProductPhoto')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ('-created_at',)


class ProductPhoto(models.Model):
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.photo

    class Meta:
        verbose_name = "Product Photo"
        verbose_name_plural = "Product Photos"
