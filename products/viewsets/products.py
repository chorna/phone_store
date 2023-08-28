from rest_framework import viewsets

from ..models import Product
from products.serializers.products import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer