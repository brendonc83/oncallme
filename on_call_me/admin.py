from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from on_call_me import models

admin.site.register(models.User, UserAdmin)
admin.site.register(models.OnCallPeriod)
