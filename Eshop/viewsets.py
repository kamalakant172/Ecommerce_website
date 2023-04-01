from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.response import Response

class UserViewsets(viewsets.ModelViewSet):
    queryset= models.signup.objects.all()
    serializer_class= serializers.UserSerializer

class CategoryViewsets(viewsets.ModelViewSet):
    queryset= models.category.objects.all()
    serializer_class= serializers.CategoryDetails

class ProductViewsets(viewsets.ModelViewSet):
    queryset= models.Product.objects.all()
    serializer_class= serializers.ProductSerializer

    