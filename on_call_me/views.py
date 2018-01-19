from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):

    return render(request, 'on_call_me/index.html', {
        'username': 'user.username',
        'first_name': 'user.first_name',
        'last_name': 'user.lastname',
        'email': 'user.email',
    })


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


"""
def view_1(request):
    # ...
    t = loader.get_template('template1.html')
    c = Context({
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR'],
        'message': 'I am view 1.'
    })
    return t.render(c)

"""