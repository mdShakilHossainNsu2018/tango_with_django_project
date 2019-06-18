from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Rango says: Hello world! <a href=about>About</a>")


def about(request):
    return HttpResponse("Rango Says: Here is the about page.<a href='/rango/'>Index</a>")
