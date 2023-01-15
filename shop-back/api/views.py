from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from api import models, serializers
from rest_framework.response import Response
from django.shortcuts import get_list_or_404

# Create your views here.
class ProductViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        model = models.Products.objects.all()
        serializer = serializers.ProductsSerializer(model, many=True)
        
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        model = get_list_or_404(models.Products.objects.all(), pk=pk)
        serializer = serializers.ProductsSerializer(model, many=True)
        
        return Response(serializer.data)

class CategoriesViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        model = models.Categories.objects.all()
        serializer = serializers.CategoriesSerializer(model, many=True)
        
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        model = get_list_or_404(models.Categories.objects.all(), pk=pk)
        serializer = serializers.CategoriesSerializer(model)
        
        return Response(serializer.data) 

class FilteredProductViewSet(ViewSet):

    def list(self, request, *args, **kwargs):
        model = models.Products.objects.filter(categories=kwargs['id'])
        serializer = serializers.ProductsSerializer(model, many=True)

        return Response(serializer.data)