from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.log_in, name= "myadmin_login"),
    path("index_myadmin/", views.index, name="index_myadmin"),
    path("myadmin-logout/", views.log_out, name="myadmin_logout"),
    path("myadmin-accounts/", views.myadmin_accounts, name="myadmin_accounts"),
]