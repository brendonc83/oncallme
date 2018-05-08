from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import OnCallPeriod
from .models import User
from on_call_me.forms import CreateOnCallPeriodsForm
from on_call_me.forms import UpdateOnCallPeriodsForm
from datetime import date, timedelta
from django.template.loader import render_to_string
from django.core.mail import send_mail
import os


@login_required()
def index(request):
    return render(request, 'on_call_me/index.html')


def oncallperiods(request):
    return render(request, 'on_call_me/userlist.html')


def weekly_email(request):

    current_month = date.today().strftime("%m")
    oncallperiodlist = OnCallPeriod.objects.filter(team_member=request.user, end_date__month=current_month)

    context = {'user': request.user, 'oncallperiodlist': oncallperiodlist}

    return render(request, 'on_call_me/weekly-oncall-email.html', context)


def send_test_email(request):

    email_from = os.environ.get('EMAIL_FROM')
    #just add a comma separated list to env variable - no quotes
    email_to = os.environ.get('EMAIL_TO')
    subject = 'oncallme Test e-mail'
    message = 'Hello, this is a test e-mail'
    from_email = email_from
    recipient_list = email_to

    current_month = date.today().strftime("%m")
    oncallperiodlist = OnCallPeriod.objects.filter(team_member=request.user, end_date__month=current_month)

    context = {'user': request.user, 'oncallperiodlist': oncallperiodlist}

    html_message = render_to_string('on_call_me/weekly-oncall-email.html', context, request=request)

    send_mail(subject, message, from_email, recipient_list, html_message=html_message)

    return render(request, 'on_call_me/index.html', context)


class UserListView(ListView):
    model = User
    template_name = 'on_call_me/userlist.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        user_list = User.objects.exclude(username='admin')
        return user_list


class OnCallPeriodCreateView(CreateView):
    model = OnCallPeriod
    form_class = CreateOnCallPeriodsForm
    template_name = 'on_call_me/index.html'
    success_url = '/oncallperiodlist'

    def form_valid(self, form):
        # Add the authenticated user into the save object
        form.instance.team_member = self.request.user

        # Get start_date from form post
        start_date = form.cleaned_data.get('start_date')

        # Get end_date from form post
        end_date = form.cleaned_data.get('end_date')

        # Calculate the week ending date and add to save object
        form.instance.week_ending = end_date + timedelta(days=6 - end_date.weekday())

        # Calculate the number of days of on call
        delta = (end_date - start_date)

        print("This is the delta: %s" % delta.days)

        # Add no of days to save object
        form.instance.days = delta.days + 1

        return super(OnCallPeriodCreateView, self).form_valid(form)


class OnCallPeriodUpdateView(UpdateView):
    model = OnCallPeriod
    form_class = UpdateOnCallPeriodsForm
    template_name = 'on_call_me/update-oncallperiod.html'
    success_url = '/oncallperiodlist'

    def form_valid(self, form):
        # Add the authenticated user into the save object
        form.instance.team_member = self.request.user

        # Get start_date from form post
        start_date = form.cleaned_data.get('start_date')

        # Get end_date from form post
        end_date = form.cleaned_data.get('end_date')

        # Calculate the week ending date and add to save object
        form.instance.week_ending = end_date + timedelta(days=6 - end_date.weekday())

        # Calculate the number of days of on call
        delta = (end_date - start_date)

        print("This is the delta: %s" % delta.days)

        # Add no of days to save object - add 1 day to include the start date
        form.instance.days = delta.days + 1

        return super(OnCallPeriodUpdateView, self).form_valid(form)


class OnCallPeriodListView(ListView):
    model = OnCallPeriod
    template_name = 'on_call_me/oncallperiodlist.html'
    context_object_name = 'oncallperiod_list'

    def get_queryset(self):
        current_month = date.today().strftime("%m")
        oncallperiodlist = OnCallPeriod.objects.filter(team_member=self.request.user, end_date__month=current_month)
        return oncallperiodlist


