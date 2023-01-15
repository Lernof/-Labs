from rest_framework import serializers
from api import models


class ProductsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    value = serializers.DecimalField(max_digits=14, decimal_places=2)
    desctiption = serializers.CharField()
    amount = serializers.IntegerField()
    is_active = serializers.BooleanField()

class CategoriesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


