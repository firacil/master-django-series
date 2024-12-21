from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home page
def home(request):
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request, 'pages/home.html')
# about as page
def about(request):
    return render(request, 'pages/about.html')

# contact as page
def contact(request):
    return render(request, 'pages/contact.html')

# services page
def services(request):
    return render(request, 'pages/services.html')