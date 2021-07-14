from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters, status

from products.models import ProductCategory, Product
from products.serializers import ProductCategorySerializer, ProductSerializer







class ProductCategoryView(ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']



