from django.contrib import admin
from on_call_me import models


admin.site.register(models.User)
admin.site.register(models.OnCallPeriod)
