"""oncallme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from on_call_me.forms import LoginForm
from on_call_me.views import UserListView
from on_call_me.views import OnCallPeriodCreateView
from on_call_me.views import OnCallPeriodUpdateView
from on_call_me.views import OnCallPeriodListView
from on_call_me.views import ManageOnCallListView
from on_call_me.views import ProcessedListView


urlpatterns = [
    path('manage-oncall', ManageOnCallListView.as_view(), name='manage-oncall'),
    path('process-oncall', views.process_oncall, name='process-oncall'),
    path('processed-list', ProcessedListView.as_view(), name='processed-list'),
    path('weekly-email', views.weekly_email, name='weekly_email'),
    path('', LoginView.as_view(template_name='on_call_me/login.html', authentication_form=LoginForm),
         name='login-home'),
    path('accounts/login/', LoginView.as_view(template_name='on_call_me/login.html', authentication_form=LoginForm),
         name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('userlist', UserListView.as_view(), name='user-list'),
    path('index', login_required(OnCallPeriodCreateView.as_view()), name='index'),
    path('update-oncallperiod/<int:pk>', OnCallPeriodUpdateView.as_view(), name='update-oncallperiod'),
    path('oncallperiodlist', OnCallPeriodListView.as_view(), name='oncallperiod-list'),
]
