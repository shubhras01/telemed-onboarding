from django.contrib import admin

from hellodoctor.models import Staff
from onboarding.models import Doctor

# Register your models here.
admin.site.register(Staff)
admin.site.register(Doctor)