from django.shortcuts import render
from django.http import HttpResponse
from on_call_me import models


def index(request):
    return HttpResponse("Welcome to index")


# Provide the username and get user details
def user_detail(request, u_id):

    user_info = models.TeamMember.objects.get(u_name=u_id)

    return HttpResponse("This is the user info %s %s" % (user_info.full_name, user_info.role))


