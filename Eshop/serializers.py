from rest_framework import serializers

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = signup
        fields = '__all__'

class OrderDetails(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = order_dtls
        fields= '__all__'

class CategoryDetails(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = category
        fields= '__all__'        

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields= '__all__'          