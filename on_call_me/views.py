from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, FormMixin
from .models import OnCallPeriod
from .models import User
from on_call_me.forms import CreateOnCallPeriodsForm
from on_call_me.forms import UpdateOnCallPeriodsForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from datetime import date, timedelta
import os


@login_required()
def index(request):
    return render(request, 'on_call_me/index.html')


def oncallperiods(request):
    return render(request, 'on_call_me/userlist.html')


def get_week_ending():

    date_today = date.today()
    end_date = date_today + timedelta(days=6 - date_today.weekday())
    week_ending = end_date

    return week_ending


def weekly_email(request):

    current_month = date.today().strftime("%m")
    oncallperiodlist = OnCallPeriod.objects.filter(team_member=request.user, end_date__month=current_month)
    print('what is this shit: %s: ' % oncallperiodlist )
    week_ending = get_week_ending()
    context = {'user': request.user, 'oncallperiodlist': oncallperiodlist, 'week_ending': week_ending}

    return render(request, 'on_call_me/weekly-oncall-email.html', context)


def send_test_email(request, html_message, context):

    email_from = os.environ.get('EMAIL_FROM')
    email_to = os.environ.get('EMAIL_TO')
    subject = 'oncallme Test e-mail'
    message = 'Hello, this is a test e-mail'
    from_email = email_from
    recipient_list = email_to.split()

    context_ = context
    html_message_ = render_to_string(html_message, context_, request=request)
    send_mail(subject, message, from_email, recipient_list, html_message=html_message_)


def process_oncall(request):
    if request.method == 'POST':
        selected_values = request.POST.getlist('oncallperiod')
        request.session['selected_values'] = selected_values
        OnCallPeriod.objects.filter(id__in=selected_values).update(processed=True)

        oncallperiodlist = OnCallPeriod.objects.filter(id__in=selected_values)

        week_ending = get_week_ending()

        context = {'oncallperiodlist': oncallperiodlist, 'week_ending': week_ending}

        html_message = 'on_call_me/weekly-oncall-email.html'

        send_test_email(request, html_message, context)

        return redirect('processed-list')


class ProcessedListView(ListView):
    model = OnCallPeriod
    template_name = 'on_call_me/processed-list.html'
    context_object_name = 'oncallperiod_list'

    def get_queryset(self):

        values = self.request.session['selected_values']
        oncallperiod = OnCallPeriod.objects.filter(id__in=values)

        return oncallperiod


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


class ManageOnCallListView(ListView):
    model = OnCallPeriod
    template_name = 'on_call_me/manage-oncall.html'
    context_object_name = 'oncallperiod_list'

    def get_queryset(self):

        date_today = date.today()
        print('This is today\'s date: %s' % date_today)

        end_date = date_today + timedelta(days=6 - date_today.weekday())
        print("The end of the week is: %s" % end_date.strftime('%d/%b/%Y'))

        oncallperiodlist = OnCallPeriod.objects.filter(processed=False, end_date__lte=end_date)
        return oncallperiodlist
