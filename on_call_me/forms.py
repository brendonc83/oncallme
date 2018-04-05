from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from on_call_me.fields import UserModelChoiceField
from on_call_me.models import OnCallPeriod
from .models import User
from django.conf import settings


# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': "Username",
                                      'type': 'text'}),
    )

    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'type': 'password'}),
    )


class CreateOnCallPeriodsForm(forms.ModelForm):
    team_member = UserModelChoiceField(queryset=User.objects.exclude(username='admin'),
                                       widget=forms.Select(attrs={'type': 'text',
                                                                  'class': 'form-control'}))

    week_ending = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                                  widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text',
                                                                                   'class': 'form-control',
                                                                                   'placeholder': 'DD/MM/YYYY'}))

    start_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text',
                                                                                  'class': 'form-control',
                                                                                  'placeholder': 'DD/MM/YYYY'}))

    end_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                               widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text',
                                                                                'class': 'form-control',
                                                                                'placeholder': 'DD/MM/YYYY'}))

    days = forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'number',
                                                              'class': 'form-control'}))

    class Meta:
        model = OnCallPeriod
        fields = ('team_member', 'week_ending', 'start_date', 'end_date', 'days',)


class UpdateOnCallPeriodsForm(forms.ModelForm):
    week_ending = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                                  widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text',
                                                                                   'class': 'form-control',
                                                                                   'placeholder': 'DD/MM/YYYY'}))

    start_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text',
                                                                                  'class': 'form-control',
                                                                                  'placeholder': 'DD/MM/YYYY'}))

    end_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                               widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text',
                                                                                'class': 'form-control',
                                                                                'placeholder': 'DD/MM/YYYY'}))

    days = forms.IntegerField(widget=forms.NumberInput(attrs={'type': 'number',
                                                              'class': 'form-control'}))

    class Meta:
        model = OnCallPeriod
        fields = ('week_ending', 'start_date', 'end_date', 'days',)
