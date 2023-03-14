from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    return render(request, 'post/hello.html')


def greet(request):
    return HttpResponse("Welcome to Django, Adeyemi")


def game(request):
    return HttpResponse("I love playing table tennis")
