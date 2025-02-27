from rest_framework import serializers
from .models import Carousel


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = "__all__"  # Include all fields