import csv

from onboarding.models import Doctor


def write_file(f, username):
    with open('csv_upload_data/doctor_data.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    with open('csv_upload_data/doctor_data.csv', 'r') as f:
        update_db_from_file(f, username)


def update_db_from_file(file, username):
    csv_reader = csv.reader(file, delimiter=',')

    for line_count, row in enumerate(csv_reader):
        if line_count == 0:
            continue

        print("line count", line_count, "line", row)
        doctor_id = row[0]
        doctor_onboarding_status = row[-1]

        doctor = Doctor.objects.filter(pk=doctor_id).first()
        doctor.onboarding_status = doctor_onboarding_status
        doctor.last_updated_staff = username
        doctor.save()
