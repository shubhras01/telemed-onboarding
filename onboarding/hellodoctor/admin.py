import csv, datetime

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse

from hellodoctor.models import Staff
from onboarding.models import Doctor

# Register your models here.
admin.site.register(Staff, UserAdmin)

DOWNLOAD_FIELDS = ["name", "email", "medical_qual", "state_authority", "contact_number", "language", "organisation_name"]


def download_sheet(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    filename = "doctor_data_" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M") + ".csv"
    attachment = 'attachment; filename="' + filename + '"'
    response['Content-Disposition'] = attachment
    # response['Content-Disposition'] = 'attachment; filename="doctor_data_%s.csv"', datetime.datetime.now()

    writer = csv.writer(response)
    writer.writerow(DOWNLOAD_FIELDS)
    for each in queryset:
       writer.writerow([getattr(each, x) for x in DOWNLOAD_FIELDS])
    return response


download_sheet.short_description = "Download csv file for selected Doctors"


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'medical_qual', 'mci', 'state_authority', 'contact_number', 'onboarding_status', 'freshdesk_agent_created')
    actions = [download_sheet]
