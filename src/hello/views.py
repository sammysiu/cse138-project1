from django.shortcuts import render

# Create your views here.

# Code taken from django project's intro tutorial
from django.http import HttpResponse

def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, world!")
    else:
        #needs 405
        return HttpResponse("This method is unsupported.", status=405)

def names(request, name):
    if request.method == 'POST':
        return HttpResponse("Hello, " + name + "!")
    else:
        #needs 405
        return HttpResponse("This method is unsupported.", status=405)