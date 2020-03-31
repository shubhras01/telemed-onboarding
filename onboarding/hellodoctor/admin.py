from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from hellodoctor.models import Staff
from onboarding.models import Doctor

# Register your models here.
admin.site.register(Staff, UserAdmin)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'medical_qual', 'mci', 'state_authority', 'contact_number', 'onboarding_status')
