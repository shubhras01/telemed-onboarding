import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

from hellodoctor.data_download import data_download
from hellodoctor.models import *


@login_required(login_url='/login/')
def download_doctors_data(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="doctor_data.csv"'

    writer = csv.writer(response)
    data_download.write_csv_file(writer, "ONBOARDED")

    return response


@login_required(login_url='/login/')
def upload_csv(request):
    if "GET" == request.method:
        return render(request, "upload_csv.html")
    # if not GET, then proceed
    try:

        print("here -> 1")

        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            return HttpResponseRedirect(reverse("myapp:upload_csv"))

        print("here -> 2")

        # if file is too large, return
        if csv_file.multiple_chunks():
            return HttpResponseRedirect(reverse("myapp:upload_csv"))

        print("here -> 3")

        file_data = csv_file.read().decode("utf-8")

        print("here -> 4")

        lines = file_data.split("\n")
        print("here -> 5")

        # loop over the lines and save them in db. If error , store as string and then display
        for lineNo, line in enumerate(lines):
            if lineNo == 0:
                continue

            fields = line.split(",")

            print("fields -> ", fields)
            doctor_id = fields[0]
            doctor_onboarding_status = fields[-1]
            Doctor.objects.filter(pk=doctor_id).set('onboarding_status', doctor_onboarding_status)

        print("here -> 6")

    except Exception as e:
        return HttpResponseNotFound("hello")

    return HttpResponseRedirect(reverse("myapp:upload_csv"))
