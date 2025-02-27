from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import login, logout
# Create your views here.

def log_in(request):
    if request.method == 'POST':
        payload= request.POST
        if payload:
            password= payload.get('password')
            user_obj= User.objects.filter(username= payload['username'])
            if not user_obj.exists():
                return render(request, 'login.html',{
                    'error_username': 'The username does not exist',
                    'title':'Login Page- Product Admin Template', # Add title
                    "dashboard": 'active'
                    })
            
            user_obj= user_obj.first()  # Converting the Queryset to Queryobject
            password_database=user_obj.password
            if check_password(password=password,encoded=password_database):
                # Redirect to the Profile Page of the User
                login(request, user_obj)
                return redirect('index_myadmin')
        
            else:
                # Redirect to the Sign In page with the Password and User name did not match
                return render(request,'login.html',{
                    'error_password':"The username and password did not match",
                    'title':'Login Page- Product Admin Template', # Add title
                    "dashboard": 'active'
                    })
    # Default title for login page
    return render(request,'login.html', {
        'title':'Login Page- Product Admin Template', # Add title
        "dashboard": 'active'
                                         }
                  )

def index(request):
    return render(request, "index_myadmin.html", {
        'title':'Product Admin - Dashboard HTML Template', # Add title 
        "dashboard": 'active'
                                                }
                  )
    
def myadmin_accounts(request):
    context = {'title': 'Accounts - Product Admin Template', 'accounts':'active', 'accounts':'active'}
    return render(request, 'myadmin_accounts.html',context)

def log_out(request):
    print("***********************")
    logout(request)
    return redirect('log_in')