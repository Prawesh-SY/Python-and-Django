from django.shortcuts import render, redirect
from django.http import HttpResponse
from carousels.models import Carousel
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import login, logout

from rest_framework import viewsets
def index(request):
    # Get the current date
    today = timezone.now().date()    
        
    # Fetch carousel items that are supposed ot be displayed today    
    carousel_items = Carousel.objects.all().filter(
        displayed_from__lte=today,
        displayed_to__gte=today,
        )
    if not carousel_items.exists():
        last_carousel_items = Carousel.objects.filter(displayed_to__lte=today).order_by('-displayed_to').first()
        if last_carousel_items:
            carousel_items = [last_carousel_items]
        else:
            carousel_items = []
    print(carousel_items)
    return render(request, "index.html", {"carousel_items":carousel_items})
    # , {"products":{"product_name":"Smart Watch",'product_price':4999.99,"description":"Get the latest, feature-rich, trending Smart watches at unbeatable price"}}
    

def sign_in(request):
    if request.method == 'POST':
        payload= request.POST
        # print(payload)
        if payload:
            password= payload.get('password')
            user_obj= User.objects.filter(username= payload['username'])
            if not user_obj.exists():
                return render(request, 'sign_in.html',{'error': 'The username does not exist'})
            
            user_obj= user_obj.first()  # Converting the Queryset to Queryobject
            password_database=user_obj.password
            if check_password(password=password,encoded=password_database):
                # Redirect to the Profile Page of the User
                login(request, user_obj)
                return redirect('profile')
        
            else:
                # Redirect to the Sign In page with the Password and User name did not match
                return render(request,'sign_in.html',{'error':"The username and password did not match"})
                pass
                
    return render(request,'sign_in.html')

def profile(request):
    return render(request,"profile.html")

def sign_up(request):
    if request.method == 'POST':
        payload= request.POST
        # Check for the repeated username or email
        if User.objects.filter(username=payload.get('username')) and User.objects.filter(email=payload.get('email')):
            error_message= "User name " + str({payload.get('username')}) + " and email " + str({payload.get('email')}) + " already exist. Please select a new user name and email"
            return render(request,'sign_up.html',{'error':error_message})
        elif User.objects.filter(username=payload.get('username')):
            error_message="User name " + str({payload.get('username')}) + " already exist. Please select a new username"
            return render(request,'sign_up.html',{'error':error_message})
        elif User.objects.filter(email=payload.get('email')):
            error_message= "Email " + str({payload.get('email')}) + " already exist. Please select a new email"
            return render(request,'sign_up.html',{'error':error_message})
        
        elif payload:
            # hashed_password = make_password(payload.get('password'))
            User.objects.create(username= payload.get('username'),password= make_password(payload.get('password')), email=payload.get('email'),first_name=payload.get('first_name'), last_name=payload.get('last_name'))
            return HttpResponse("<h1>Congrats!!!</h1>")
            
        else:
            return HttpResponse("Some error occured")
    return render(request,'sign_up.html')

