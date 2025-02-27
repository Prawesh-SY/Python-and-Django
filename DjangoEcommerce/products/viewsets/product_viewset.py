from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .. models import Productasperhtml
from ..serializers.product_serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated


# ViewSets define the view behavior.
class ProductasperhtmlViewSet(viewsets.ModelViewSet):
    queryset = Productasperhtml.objects.all()
    permission_classes= [IsAuthenticated]
    serializer_class = ProductSerializer
    
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name', 'des','category__name','price']  # Fields to enable search
    filterset_fields = {
        'category__name': ['exact', 'icontains'], 
        'price': ['gte', 'lte'],
        
        }  # Fields to enable filtering
    ordering_fields = ['id','name', 'price', 'created_at']  # Fields to enable sorting
    ordering = ['name']  # Default ordering