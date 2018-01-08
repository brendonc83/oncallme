from django.shortcuts import render
from django.http import HttpResponse


#def index(request, u_id):
#    return HttpResponse("You're looking at question %s. " % u_id)


def index(request):
    return HttpResponse("Welcome to index")
