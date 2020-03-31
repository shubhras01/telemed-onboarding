from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from hellodoctor.models import Staff
from onboarding.models import Doctor

# Register your models here.
admin.site.register(Staff, UserAdmin)
admin.site.register(Doctor)
