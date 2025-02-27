from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers
from . viewsets.product_viewset import ProductasperhtmlViewSet

router = routers.DefaultRouter()


urlpatterns = [
    path('api/', include(router.urls)),
    path("", views.product_view, name= "products"),
    path("add_product/", views.add_product, name="add_product"),
    path("edit_product/", views.edit_product, name="edit_product"),
    path("add_product_form/", views.add_product_form, name= "add_product_form"),
    path("edit_product_form/", views.edit_product_form, name= "edit_product_form"),
    path("filter_product/", views.filter_product, name= "filter_product"),
    path('edit_product/<int:product_id>/', views.edit_product_specific, name='edit_product_specific'),
    path('product-api/', views.product_api, name="product_api"),
    
    path('products/<int:pk>', views.product_detail, name="Product_detail"),
]