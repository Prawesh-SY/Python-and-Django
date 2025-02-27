from django.shortcuts import render
from django.utils import timezone
from . models import Carousel

# Create your views here.
def carousels(request):
    
    # Pass the carousel items to the template
    return render(request,"carousel.html")