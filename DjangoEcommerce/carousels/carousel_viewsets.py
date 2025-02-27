from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from .models import Carousel
from .carousel_serializer import CarouselSerializer

# Create the ModelViewSet child class to define the view behavior of the Carousel model
class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer
    
    # Create new Carousel
    
    # Read all the Carousel created
    # Update an exsisting Carousel
    # Delete an existing Carousel