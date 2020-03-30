from hellodoctor.models import Doctor


def write_csv_file(writer, doctor_onboarding_status):
    fields = ['id', 'name', 'onboarding_status']

    # write the headers
    writer.writerow(fields)

    # Get the onboarding status to be filtered by
    filter_by_status = Doctor.DOCTOR_ONBOARDING_STATUS[0][0]
    for onboarding_status in Doctor.DOCTOR_ONBOARDING_STATUS:
        if onboarding_status[1] == doctor_onboarding_status:
            filter_by_status = onboarding_status[0]

    # Get all the doctors for the status
    doctors = Doctor.objects.filter(onboarding_status=filter_by_status)

    # get data from database.
    for doctor in doctors:
        row_data = list()
        for field in fields:
            row_data.append(getattr(doctor, field))

        writer.writerow(row_data)
