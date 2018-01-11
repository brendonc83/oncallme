from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import TeamMember


def index(request):
    return HttpResponse("Welcome to index")


"""
# Provide the username and get user details
def user_detail(request, u_id):
    try:
        user_info = (TeamMember.objects.get(u_name=u_id))
        context = {'user_info': user_info}
    except TeamMember.DoesNotExist:
        raise Http404("TeamMember does not exist")
    return render(request, 'on_call_me/index.html', context)
"""

"""
# Provide the username and get user details
def user_detail(request, u_id):
    print(u_id)
    user_info = get_object_or_404(TeamMember, u_name=u_id)
    context = {'user_info': user_info}
    return render(request, 'on_call_me/index.html', context)
"""


class TeamMemberDetailView(generic.DetailView):

    model = TeamMember
    template_name = 'on_call_me/index.html'
