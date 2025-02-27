from django.contrib import admin
from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from .carousel_viewsets import CarouselViewSet

router = DefaultRouter()
# router.register(r'carousels', CarouselViewSet)


urlpatterns = [
    path("", views.carousels, name= "carousels"),
    # path('', include(router.urls))
]