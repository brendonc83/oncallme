from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from on_call_me.models import OnCallPeriod
from django.conf import settings
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _


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

    start_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text',
                                                                                  'class': 'form-control',
                                                                                  'placeholder': 'DD/MM/YYYY'}))

    end_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                               widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text',
                                                                                'class': 'form-control',
                                                                                'placeholder': 'DD/MM/YYYY'}))

    def clean(self):
        cleaned_data = super(CreateOnCallPeriodsForm, self).clean()
        end_date = cleaned_data.get('end_date')
        start_date = cleaned_data.get('start_date')

        if end_date and start_date:
            if end_date < start_date:
                raise ValidationError(_('End date cannot be before the start date'), code='invalid')
        return cleaned_data

    class Meta:
        model = OnCallPeriod
        fields = ('start_date', 'end_date',)


class UpdateOnCallPeriodsForm(forms.ModelForm):

    start_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text',
                                                                                  'class': 'form-control',
                                                                                  'placeholder': 'DD/MM/YYYY'}))

    end_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,
                               widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text',
                                                                                'class': 'form-control',
                                                                                'placeholder': 'DD/MM/YYYY'}))

    def clean(self):
        cleaned_data = super(UpdateOnCallPeriodsForm, self).clean()
        end_date = cleaned_data.get('end_date')
        start_date = cleaned_data.get('start_date')

        if end_date and start_date:
            if end_date < start_date:
                raise ValidationError(_('End date cannot be before the start date'), code='invalid')
        return cleaned_data

    class Meta:
        model = OnCallPeriod
        fields = ('start_date', 'end_date',)
