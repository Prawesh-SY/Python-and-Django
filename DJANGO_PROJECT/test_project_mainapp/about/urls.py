from . import views
from django.urls import path
urlpatterns = [
    path("aboutus/", views.about, name = "about")
]
