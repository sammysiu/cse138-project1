from django.shortcuts import render

# Create your views here.

# Code taken from django project's intro tutorial
from django.http import HttpResponse

def msg(request, msg):
    if request.method == 'POST':
        return HttpResponse("POST message received: " + msg)
    else:
        #needs 405
        return HttpResponse("This method is unsupported.", status=405)