import csv

from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse

from hellodoctor.data_download import data_download


# Create your views here.
@login_required(login_url='/login/')
def on_login(request):
    return HttpResponse("<h1>Hello World</h1>")


@login_required(login_url='/login/')
def download_doctors_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="doctor_data.csv"'

    writer = csv.writer(response)
    data_download.write_csv_file(writer, "NOT_ONBOARDED")

    return response
