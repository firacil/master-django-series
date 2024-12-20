from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home page
def home(request):
    return HttpResponse("<h1>Home Page</h1>") 
# about as page
def about(request):
    return HttpResponse("<h1>About Us Page</h1>") 

# contact as page
def contact(request):
    return HttpResponse("<h1>Contact us Page</h1>") 

# services page
def services(request):
    return HttpResponse("<h1>Services Page</h1>") 