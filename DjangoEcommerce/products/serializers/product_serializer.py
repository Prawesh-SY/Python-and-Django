
from django.urls import include, path
from rest_framework import routers, serializers, viewsets
from products.models import Productasperhtml

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productasperhtml
        fields = '__all__'
