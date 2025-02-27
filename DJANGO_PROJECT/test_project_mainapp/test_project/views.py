from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")
# def sign_up(request):
#     return render(request,"sign_up.html")