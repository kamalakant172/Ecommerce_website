from rest_framework import serializers

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = signup
        fields = '__all__'
