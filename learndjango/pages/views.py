from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home page
def home(request):
    
    # adding some context variables to html dynamically
    context = {
        "page_name": "Home Page",
        "title": "Home"
    }
    return render(request, 'pages/home.html', context)
# about as page
def about(request):
    context = {
        "page_name": "About us Page",
        "title": "About"
    }
    return render(request, 'pages/about.html', context)

# contact as page
def contact(request):
    context = {
        "page_name": "Contact us Page",
        "title": "Contact"
    }
    return render(request, 'pages/contact.html', context)

# services page
def services(request):
    context = {
        "page_name": "Services Page",
        "title": "Services"
    }
    return render(request, 'pages/services.html', context)